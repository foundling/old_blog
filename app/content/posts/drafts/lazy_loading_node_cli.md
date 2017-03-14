Recently, I was working on a command-line application to manage the data acquisition process for a scientific study.  As the subcommands grew in complexity, the load time increased quite noticeably. I went about figuring out how to fix it and I'd like to write a little bit about that process.
 
The cli app has a straightforward standard sub-command structure: 

    cmd sub-cmd [ arguments ... ] [ options ... ]

The sub-commands are where the main functionality is. The app exposes five of them:

    cmd register
    cmd query <name> <date-range>
    cmd show <project metric>
    cmd stats
    cmd update

## Finding a Command Parsing Library

I decided to use [commander.js](https://github.com/tj/commander.js) to parse the commands. Commander is a simple and fairly transparent library for building simple to moderately complex command-line interfaces. The library was written by Tj Holowaychuk, author of Express. 

## Modularity: Only Gets You Half the Way There

Wanting to keep this application modular for testing, I broke the functionality into atomic units and assembled these into top-level function modules for each sub-command. Below is the cli entry point that is run on invocation of the cli app. There I pull in the modules my cli requires, register them as callbacks for their respective sub-commands, nd then start the parser which parses the command line input and calls the appropriate callback.

Here is what my initial `index.js` looked like: 

    const cli = require('commander');
    const { register, query, show, stats, update } = require('./commands');

    cli
        .command('query')
        .description('gives you stats.')
        .action(stats);

    cli
        .command('run')
        .description('runs the app')
        .action(run);

    cli
        .command('query')
        .description('queries the API')
        .action(query);

    cli
        .command('health')
        .description('checks the health of various things')
        .action(health);

    cli
        .command('update')
        .description('updates the app')
        .action(update);

    cli.parse(process.argv);

## I'm Loading Everything Every Time

Once I started registering these modules with `commander`, the execution time for just the base command that prints a help page was something like 8 seconds (granted my computer is getting up there in years). This is because the `index.js` file pulls in the dependencies for the entire application and loads them all synchronously before parsing the command. And while the OS caches recently loaded modules, bringing subsequent invocations of the command down to just a few hundred milliseconds, the cli would most likely be used sporadically, negating the benefits of the cache.  In the average use case, the performance was not good.

## Loading Just the Libraries You Need

In order to cut the load time down, I decided to restrict the loading of dependencies to the just those required by the sub-command being executed. This comes down to shifting the scope and timing of the require call so that it gets called as part of the callback associated with a command rather than on the execution of the top level `index.js` entry-point file. While `commander` allows for independent git-style subcommands, I found that that design didn't fit my needs for two reasons:

1) The subcommand files need to follow a specific naming and location convention. If the command is `cmd subcmd`, then there needs to be an executable file named `subcmd.js` in the directory where `cmd` is located. 

2) The subcommand module is `exec`'ed by Node and thus needs to take the form of a script, not a module. I needed my sub-command files to take the form as a module for testing purposes.

I ended up writing a utility function like this:

    function delayedRequire(depName) {

        return function() {
            require(`./${ depName }`);
        }

    }

That solves the lazy-loading issue. Now instead of registering the submodule command directly with commander (which requires the submodules and their dependencies to be imported first), I register the result of the `delayedRequire` function call, which produces a callback that requires the dependency:

    cli
        .command('stats')
        .description('gets stats')
        .command( delayedRequire('stats') );

I've moved the scope and timing of the require call from the initial `index.js` execution to the execution of a command callback by `commander`.

The final issue still left to resolve was to pass the arguments from commander to my command callback. Commander is going to pass the parsed arguments to the function registered by `.command`, which is `delayedRequire`'s inner function. That inner function should do something with these arguments.

    function delayedRequire(depName) {
        
        return function(...args) {
            const entryPoint = require(`./commands/${ depName }`);
            entryPoint(...args);
        };

    }

Here's what I came up with (including a few additional variations):


    const cli = require('commander');
    const basepath = './commands';
    const makeLoader = function(name) {

        return function(...args) {

            let entryPoint = require(`${basepath}/${name}`);
            entryPoint.(...args);

        };

    };

    const callbacks = [

        'stats', 'run', 'query', 'health', 'update'

    ]
    .reduce((o, dep) => {

       o[dep] = makeLoader(dep);
       return o;

    }, {});

    { stats, run, query, health, update } = callbacks; 

    cli
        .command('stats')
        .description('gives you stats.')
        .action(stats);

    cli
        .command('run')
        .description('runs the app')
        .action(run);

    cli
        .command('query')
        .description('queries the API')
        .action(query);

    cli
        .command('health')
        .description('checks the health of various things')
        .action(health);

    cli
        .command('update')
        .description('updates the app')
        .action(update);


    cli.parse(process.argv);
