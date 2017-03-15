Recently, I was working on a command-line application to manage the data acquisition process for a scientific study.  The app performs a bunch of disparate tasks that require libraries for: 

+ Handling OAuth2-based subject registration on a local webserver 
+ HTML templating
+ Querying FitBit's API
+ Reading from and writing to a local database
+ Async control flow
+ Date and time manipulation and formatting
+ Colorizing stdout output
+ Functional programming 

As I moved toward completion of the project and the sub-command modules grew in size and complexity, I noticed that the load time increased to about 8 seconds even to just show the help screen. I was able to get it down to less than a second without too much effort and I'd like to share a little bit about how I did that. 

## The Interface

The cli app has a standard sub-command structure: 

    cmd sub-cmd [ arguments ... ] [ options ... ]

The sub-commands are where the main functionality is. The app exposes four of them:

    cmd register
    cmd query <name> <date-range>
    cmd stats
    cmd update

I decided to use [commander.js](https://github.com/tj/commander.js) (written by TJ Holowaychuk, author of Express) to handle the parsing of command-line input. It's a simple and intuitive library that fits the use case for simple to moderately complex cli apps in Node. 

## Modularity Only Gets You Half Way There

In order to keep the application modular and easily testable, I broke the functionality into top-level modules that correspond to the sub-commands `register`, `query`, `stats` and `update`. Each of these was made up of a variety of custom and 3rd-party sub-modules. Below is the entry point that is executed when the cli app is run on the command line. I'm pulling in the top-level sub-command modules, registering each on the `commander` cli object as a callback for its respective sub-command, and then I call the parser to parse the stdin input and call the appropriate callback.

Here is a pared-down version of my app's directory structure:

    app/
        cli/
            index.js // app entry point
            commands/
                index.js // bundles the sub-commands into a single module and exports them
                register.js
                query.js
                stats.js
                update.js


Here is what my initial `index.js` looked like when it took 8 seconds to load: 

    const cli = require('commander');
    const { 

        register,   
        query, 
        stats, 
        update 

    } = require('./commands'); // pulls in modules exported from app/commands/index.js

    cli
        .command('register')
        .description('register subject for study.')
        .action(register);

    cli
        .command('query <subject_id>')
        .description('query data for subject.')
        .action(query);

    cli
        .command('stats')
        .description('show study statistics.')
        .action(stats);

    cli
        .command('update')
        .description('pull in new changes to the app')
        .action(update);

    cli.parse(process.argv);

## I'm Loading Everything, Every Time

The problem is simply that in `index.js`, I'm pulling in the dependencies for the entire application and loading them all synchronously before parsing the command. So, even if you're looking for the help screen, when the app runs, this is what would be loaded:


        "async": "^2.1.4",
        "body-parser": "^1.15.2",
        "colors": "^1.1.2",
        "commander": "^2.9.0",
        "concat-map": "0.0.1",
        "cors": "^2.8.1",
        "express": "^4.14.0",
        "fitbit-node": "foundling/fitbit-node",
        "hbs": "^4.0.1",
        "moment": "^2.16.0",
        "nedb": "^1.8.0",

Well, these dependencies, *plus* the dependencies that they have, *plus* the sub-modules I wrote specifically for the app. While the OS caches recently loaded modules, bringing subsequent invocations of the utility down to just a few hundred milliseconds, the utility would be used usually once per session and sporadically, negating the benefits of the cache.  So in the average use case the performance was ... *bad*.

## Loading Just the Libraries You Need

In order to cut the load time down, I had to pull in only what was needed for the one sub-command being executed. This comes down to shifting the scope and timing of the `require` call so that it is executed in the callback for that single sub-command. 

I should mention that `commander` supports git-style sub-commands, but I found that that design didn't fit my needs for two reasons:

1) The sub-command files need to follow a specific naming and location convention in order for `commander` to execute them. If the command is `cmd subcmd`, then there needs to be an executable file named `cmd-subcmd.js` in the directory where `cmd.js` is located. 

2) The subcommand module is `exec`'ed by Node and thus needs to take the form of a script, not a module. I needed my sub-command files to take the form as a module for testing purposes.

Both of these issues could have been worked around, but I felt that it was easy enough to work lazy sub-commands into my project with just a few lines of code. I ended up writing a utility function like this:

    function delayedRequire(depName) {

        return function() {
            require(`./${ depName }`);
        }

    }

`delayedRequire` takes a dependency name and return a function that requires that dependency. That solves the lazy-loading issue. Now instead of registering the submodule command directly with commander (which requires all submodules and their dependencies to be imported first), I register a function that does both the `require` and module execution.

    // if the user runs 'cmd stats' on the command line, 
    // then just the stats module is loaded
    cli
        .command('stats')
        .description('gets stats')
        .command( delayedRequire('stats') );

## Handling The Arguments 

The final thing to work out was to forward the arguments passed from `commander` to the triggered callback. Since the new function both requires the sub-command module and calls it, we need to pass the arguments to the `require`ed module manually. Here are is the approach in both ES5 and ES2015.

    // es5 way
    function delayedRequire(depName) {
        
        return function() {

            // .apply is an alternate way of calling a function
            // it takes an array or array-like object of arguments

            // arguments is a special quasi-array keyword pointing to the list of 
            // arguments passed to any function

            const entryPoint = require(`./commands/${ depName }`);
            entryPoint.apply(entryPoint, arguments);

        };

    }

    // the es2015 way
    function delayedRequire(depName) {
        
        // use rest parameter syntax to capture variable parameter lists as a single array

        return function(...args) {

            // destructure the array into its individual arguments in order to
            // call the entryPoint function as usual, on the individual arguments

            const entryPoint = require(`./commands/${ depName }`);
            entryPoint(...args);

        };

    }

    // the less clear ... or  'succinct' ... es2015 way :)
    const delayedRequire = (depName) => (...args) => require(`./commands/${ depName }`)(...args);

Here's a more complete version of what I came up with. Notice that the syntax for the `commander` callback registration is basically the same as it was in the beginning:

    const cli = require('commander');
    const basepath = './commands';
    const makeLoader = function(name) {

        return function(...args) {

            let entryPoint = require(`${basepath}/${name}`);
            entryPoint.(...args);

        };

    };

    // build an object of loaders from an array of module names
    // destructure the result into module bindings.
    const { 

        register, 
        query, 
        stats, 
        update 

    } = [ 

        'register', 
        'query', 
        'stats', 
        'update' 

    ].reduce((o, dep) => {

       o[dep] = makeLoader(dep);
       return o;

    }, {});

    // then register the module bindings with their corresponding commands
    cli
        .command('register')
        .description('register subject for study.')
        .action(register);

    cli
        .command('query <subject_id>')
        .description('query data for subject.')
        .action(query);

    cli
        .command('stats')
        .description('show study statistics.')
        .action(stats);

    cli
        .command('update')
        .description('pull in new changes to the app')
        .action(update);

    // parse the stdin input and route control to the right callback 
    cli.parse(process.argv);
