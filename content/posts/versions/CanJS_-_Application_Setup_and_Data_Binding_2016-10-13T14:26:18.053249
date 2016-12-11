# CanJS Series - Part 1: Application Setup and Data Binding

### Goal

The goal of this tutorial is to introduce the process of building a simple CanJS page from scratch using the [StealJS](http://stealjs.com/) module loader. It will cover:

+ dependency installation
+ setting up our package.json file, which is crucial to using `steal.js`
+ using the `steal` build function in our JavaScript code
+ loading templates and live-binding data objects to them

### Limitations

This tutorial takes place mostly on the command-line and (currently) has a Linux/BSD/Mac OS bias.

### Why is this tutorial using CanJS? 

I started developing with CanJS because it was what a previous workplace used as their front-end JavaScript framework.  CanJS doesn't have the market share of Angular, React or Ember, but it has a steady user-base and is both fully-featured, fast and lightweight. And if you encounter an issue, the CanJS community, including the core contributors, are very quick to help.  But I decided to write this series because I felt, after enough frustration, that the world could use some additional CanJS resources from a different perspective. As it is right now, much of the documentation comes from Bitovi, whose docs, though extensive, are somewhat dispersed and occasionally confusing. This series attempts to start with tooling and basic `can`-isms and move toward a more complex, component-based application.

With that said, here are some additional resources that you might find useful:

+ Bitovi's [YouTube channel](https://www.youtube.com/channel/UC_HPFLeKzJNLOUnLc_3311Q/videos)
+ The [Guides](https://canjs.com/guides/index.html)
+ The [API Documentation](https://canjs.com/docs/index.html)
+ The [Forums](http://forums.donejs.com/c/canjs) 
+ The CanJS [GitHub page](https://github.com/canjs/canjs) 

### On Using a Module Loader

Why are we using a module loader instead of script tags for our code?

- **Organization**: Modules are beneficial for complex architectures because they allow you to write isolated units of code and inject them easily into different parts of your application. This affords you greater organization and testability. Before module loaders were available, it was a best practice for JavaScript developers to wrap a module in an [IIFE](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression) to isolate it from the global namespace, giving it module-like functionality. StealJS is one of many libraries that provide first-class module support in a JavaScript environment (StealJS can do a lot more than this, though).  

- **Dependency Management**: a complex application will require dependencies that require other dependencies that require other dependencies, etc. As the number of modules grow, the app's dependency relationships become increasingly difficult to maintain. A module loader will take care of the dependency tree for you, so you can focus on building your app instead of constantly having to re-order script tags. 

- **Speed**: In the case of StealJS, which is an asynchronous module loader, the app is able to start executing sooner because the module loading process is non-blocking, so modules can be loaded in 'parallel'. 

### The Demo Application

In terms of functionality, the demo app will be very simple, merely demonstrating how to sync a view with an underlying data object. We will use CanJS's declarative event binding syntax to demonstrate that interactions with the view change the data model, which in turn syncs with the view.

The emphasis here is much more on StealJS and the central role of the `package.json` file when building an app with StealJS. I'll also cover the asynchronous structure of the steal function as well as the syntax for importing various types of modules.

### Installing Node and npm

If you don't have node on your platform, you can download it from the [NodeJS website](https://nodejs.org/en/download/). The platform-specific installations currently ship with `npm`, so if you use one of those, there is no need to install `npm`.

Make sure npm is upgraded to its latest version by running `npm install npm -g`.
  
## Installing Node Version Manager

Node Version Manager (nvm) lets you switch between NodeJS versions without any hassle. Nvm isn't a hard requirement for this tutorial, but it will make using Node in the future a little easier. If you are running OS X or Linux, follow the installation instructions for nvm [here](https://github.com/creationix/nvm/blob/master/README.markdown). If you are running Windows, the previous link has some links to Windows-friendly nvm alternatives. Also, note that the `nvm` package installable through the `npm` command is not the correct package. 
  
### App Directory Structure 

Here is what our folder structure will look like:

````
demo_app/
    app/
        app.js
        app.stache
        app.less
    index.html
    node_modules/
        # modules downloaded via 'npm install [module name]' command
    package.json
````

We will manually create everything except for the  `node_modules` directory and the `package.json` file.

#### Create our application directories and files

Change to the directory where you want to put this application and run the following commands:

+ `mkdir -p demo_app/app`
+ `touch demo_app/{index.html,app/app{.stache,.js,.less,_test.js}}`
+ `tree demo_app` (to verify you have the right structure)


#### Change directory into your application root, `demo_app`

Type `cd demo_app` so you are now in the `demo_app` directory. If you run `pwd`, it should show you a filepath ending with 'demo_app'.

#### Initialize your app as a package

Before you start installing modules, it's important to create a `package.json` file so our installations are automatically tracked. We can do that easily with this command:

`npm init`

It will present you with a lot of options, none of which are important for this application. So, press `Enter` to accept each default, then type `yes` to accept them and write the `package.json` file to your application's root directory, which should be your current directory. 


#### `npm install` commands explained

Here are the commands we will use to install packages

+ `npm install [module]` (install module in our local `node_modules` folder)
+ `npm install [module] -g` (install module globally)
+ `npm install [module] --save` (install module and save it to our package.json as an application dependency)
+ `npm install [module] --save-dev` (install module and save it to our package.json as a developer dependency)

A dependency is a module that the application must have in order to run.  A developer dependency is a module that isn't strictly necessary to run the app, but is useful development tool for building the app with (for example, testing tools like Mocha and Chai).

#### Install the essential project dependencies

Let's install `can` and `steal` as regular application dependencies:

`npm install --save can steal`

#### Install a global development server if you don't already have it  

`npm install -g http-server`

#### Setting up the `index.html` and the `app/app.js` files

Open the `index.html` file and add or copy the following to it:

````html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
</head>
<body>
    <div id="app"></div>
    <script src="node_modules/steal/steal.js"></script>
</body>
</html>
````

Notice the script tag at the end of the body tag.  This references the `steal.js` loading script. On the page load, `steal.js` will look in our `package.json` file for information about where to find the main application file and which dependencies it should treat as node modules when load the dependencies we specify in our code.

Open the `package.json` file and set the `main` entrypoint (the default is `index.js`) to `app/app`. This indicates that the application entrypoint is `app.js` inside of the `app` directory. The `.js` extension isn't necessary.

#### Testing that everything loads correctly

Run `http-server` from the root of your project directory, `demo_app`, and copy the `localhost` port location it outputs into your web-browser (StealJS needs a server to handle its request and won't load from the filesystem).  With no arguments, `http-server` should load at `localhost:8080`. If you need a different port, you can use the `-p` flag to specify an alternate.

Once you've loaded that page (which should be blank, we haven't added any code), open your web browser's developer console and ensure there are no `steal.js` or `app.js` errors. You can ignore `favicon.ico` 404 errors.

### Using StealJS 

StealJS is exposed as a single function that accepts as arguments:

+ a list of file paths as strings
+ a final callback function whose arguments are the loaded dependencies found at filepaths. 

It loads the modules located at the paths asynchronously but waits until they're all loaded.  At that point, you access them via the callback under the name spaces that you are able to  use them in a callback.  Here is a conceptual sketch demonstrating the conventions for specifying the three types of dependencies: 

+ node modules
+ absolute user module 
+ relative user module

**Note**: `steal` is also callable as a Promise, but that isn't covered in this tutorial.


Here is a conceptual `steal` call to demonstrate the three conventions above.  Note two things:

+ the order of the dependency paths is consistent with the order of the arguments passed into the callaback, except in the case of the `.less` file, which is not given a namespace because it would provide no benefit. 
+ The `!` at the end of the `.stache` and `.less` filepaths indicates that `steal` should not try to load them as JavaScript files.


````javascript

steal(

    'nodemodule',
    'absolute/user_module.js',
    './relative_user_module.js',
    './app.stache!',
    './app.less!',

    function(

        nodeModule,
        absoluteUserModule,
        relativeUserModule,
        appTemplate
        appStyle 
        
    ) {
        // code goes here
    }
);

````


#### Things to note about StealJS paths 

+ We use `npm install can --save` because even if you installed `can` and it's in the `node_modules` directory, you will still get an error from `steal` if it's not listed in your `package.json` file as well.  This is because StealJS uses this file to specifically resolve dependencies in your `node_modules` directory. This is why it's important to run `npm init` before you start installing anything, and to use the `--save` and `--save-dev` flags to track those dependencies for `steal`.
+ Node modules are specified by name, not as file paths. 
+ Paths that start with './' are relative to the directory of the file you're working in.
+ Paths that do not start with './' are relative to the directory containing your application's `package.json` file
+ non-JavaScript files should be suffixed with a '!'.
+ Stache files require a namespace in the steal callback in order to be used, but less/css files take effect whether you give them a namespace or not (and, in fact, you can't access the less/css file's contents this way).


#### The Demo Application

Now, let's get to work!

Open your `app/app.js` file and add the following:

````javascript
steal(
    'can',
    function(can){
        console.log(can);
    }
);

````

Here, I'm just logging the `can` object to confirm it's present. When I run this in google Chrome, I see this in the console:

````
Object {global: Window, VERSION: "@EDGE", isNode: false, isBrowserWindow: true, isWebWorker: false…}  
````

#### Creating and loading a stache template

To add a stache template, we need to create a `.stache` file. Earlier, we created a file called `app.stache` inside of the `app` directory. Open that file and add the following:

````html
<p>Hey <span>{{ name }}</span>, you are <span>{{ description }}</span>!</p>
````
Now open `app/app.js` and add a reference our  `app.stache` file:

````javascript
steal(
    'can',
    'app.stache!',
    function(can, appTemplate){
        console.log(appTemplate);
    }
);
````

Here i'm logging the `appTemplate` object to see what it is.  In the console, you'll see it's a function.  That is because when we reference a `.stache` file, what is returned is a function that now includes the template and is looking for a data object to merge with the template's parameters. This data argument is considered the 'context' in which the view file lives.

#### Attaching the stache template to our page

Let's use jQuery to attach the template to the `div` in our `index.html` with an id of `app`.

````javascript
steal(
    'can',
    'stache',
    function(can, appTemplate){
        $('#app').append(appTemplate);
    }
);
````

Consider this a gotcha.  The template renders (with notable blanks where the variable substitution should happen), but we haven't injected any data into it the template. We need to do that in order for the `.stache` file to make the variable substitions.  


````javascript
steal(
    'can',
    'stache',
    function(can, appTemplate){

        var data = {
            name: 'Alex',  
            adjective: 'cool',
            altAdjective: 'excellent'
        };

        var compiledTemplate = appTemplate(data); 
        $('#app').append(compiledTemplate);
    }
);
````

Consider this another gotcha! We see the data being merged with the template, so that's a success.  But what we've done wrong is compile the `appTemplate` rendering function with a vanilla JavaScript object.  It won't cause an error, but we also won't be able to achieve our goal of modifying the data underlying the view via interactions with view. We want to pass an object to `.stache` whose values are observable so that when an event happens to an element, and the handler function in our code modifies the data we've provided, we can see the result instantly in our view.

CanJS provides us with a few data structures for this, but I'm only going to talk about the `can.Map` in this part.  A `can.Map` is a data structure that wraps observable behavior around an ordinary JavaScript object.  By observability, I mean that a change in the model is reflected in the view, and a change in the view is reflected in the model. 

Let's make the following modifications to our code:

````javascript
steal(
    'can',
    'stache',
    function(can, appTemplate){

        // data is now an instantiated can.Map object
        var data = new can.Map({
            name: 'Alex',  
            description: 'very cool',
            altDescription: 'quite excellent'
        });

        var compiledTemplate = appTemplate(data); 
        $('#app').append(compiledTemplate);
    }
);
````

Now we are out of gotcha land! But we still have to add some behavior to our page. 
#### Adding description-swapping behavior to your view

If you reload your browser, nothing should have changed since the last modification we made. That is because we haven't attached any behavior to our view data.  So let's add a function called `swap` that swaps the `description` and `altDescription` properties on our `can.Map`. 

Open your `app/app_template.stache` file and add a `can-click` attribute to the `<span>` tag that holds the `attribute` parameter, giving it an event handler name of `swap`. It should look like this:

````html
<p>Hey <span>{{ name }}</span>, you are <span can-click="swap">{{ description }}</span>!</p>
````

Now in your `app/app.js` file, add a function to the `data` map, just below `altDescription`, that swaps `description` with `altDescription`:


````javascript
steal(
    'can',
    'stache',
    function(can, appTemplate){

        // data is now an instantiated can.Map object
        var data = new can.Map({
            name: 'Alex',  
            description: 'very cool',
            altDescription: 'quite excellent',
            swap: function() {
                var tmp = this.attr('description'); 
                this.attr('description', this.attr('altDescription'));
                this.attr('altDescription', tmp);
            }

        });

        var compiledTemplate = appTemplate(data); 
        $('#app').append(compiledTemplate);
    }
);
````

#### The arguments that `swap` receives 

We didn't explicitly pass any parameters to `swap`, but if you add this line into your swap function,

````javascript
console.log(arguments);
````

you should see something like `[Object, jQuery.fn.init[1], j…y.Event]` in the output of your console. This indicates that three arguments are passed to can DOM event handlers: 

+ The data 'context' of your event handler  
+ The jQuery-wrapped element
+ The jQuery-wrapped event

It is important to note that the data 'context' of the event handler is not a `can.Map`, so you unfortunately cannot modify it via the `attr` method or expect it to reflect any changes in your view.  It is a vanilla JavaScript object. However, you can do some useful things with it which we will explore in future tutorials (hint, call the `.indexOf` method on a `can.List` to get its index, should you wish to splice it).


#### What is `this` ? 

We are accessing the values in `data` using `this`.  Because `can.Map` is a constructor function, the execution context for its event handling method `swap` will be the object itself, so `this` will accordingly refer to the `data` object itself. So that is why we use `this` to refer to the properties on our `data` object.

#### Using `attr` 

Forgetting to use `attr` is a common CanJS gotcha.

We use the `attr` method to access the *observed* values that the `can.Map` data structure provides for us.  Remember to *always* use `attr` when working with CanJS  data structures, or you will implicitly lose that observability and be stuck wondering why your view isn't updating. 

#### The final result

Reload your browser and click on the description. If all goes well, you should see a the description alternate between the value of the `description` property and the `altDescription` property as they were defined on the first instantiation. 

