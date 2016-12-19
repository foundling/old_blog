Functional methods like `.map`, `.filter`, `.reduce`, `.some` and `.all` can bring clarity and brevity to the parts of your code that transform data.

Below, I'm sending some fictional dataset through a series of functional methods calling named callbacks. See how clear it can be?

````
dataset
    .filter(hasX)
    .map(transformToY)
    .some(isZ);

````

Here, we've defined our criteria for that first filter callback completely within the body of the callback function (well, plus the arguments we know reduce will be giving us), so that's its own execution context [0]. But in a lot of practical cases, the criteria for the transformation of a given data set requires input from multiple execution contexts. Let's take `hasX` for example. What if this `X` that a given datum could have is something dynamic like a parameter passed in from an outer context? We'd love to pass that `X` into `.filter`'s callback, but that's not how `.filter` works, it only accepts a single item from the dataset in any given iteration.

What are we to do? 

Well, we can always refer to that extra parameter from within the `hasX` function definition if we want to keep that variable in an outer scope. Here's a potential definition of `hasX` using that idea:

````
const thing = 'init';
// codes ...
const hasX = (datum) => datum.includes(thing);
````

That's fine, right?

Well, I'd argue it's not, for three reasons:

+ Legibility: As it stands, the only thing that's clear where `thing` comes from is ... not here.
+ Portability: As it stands, `hasX` is like your good but difficult friend `Y`.  You can't just take him *anywhere* because he's always going on about something that no one's ever heard of.
+ Testability: I'd like to drop `hasX` off at my test suite, but the value to which `thing` refers is lexically [1] scoped, so the value is *there* but inaccessible.

So let's make `hasX` a truly great, capable, adaptable citizen in your code.

We'll keep the idea of closure [2], but greatly reduce the lexical distance between the value closed over and the closing-over function by composing two functions that work together to filter out filenames that don't have `X`. This new version of `hasX` should accept an argument, the `X`, and return another function that accepts another argument, the filename. From the inner function, which is executed strictly after the outer function, we will by then have both values we need in order to check whether a datum has the property we're looking for. One function returning another. Two functions working together hand-in-hand. Things have never looked so great.

````
const hasX = (thing) => {
   
    return (datum) => {
        return datum.includes(thing);
    }
};
````

And now, when you get around to using `hasX`, you can write this:

````
dataset
    .filter(hasX('Z'))
    .map(transformToY)
    .some(isZ);

````

That is clean af! And why don't we, in good aesthetic taste, rename the function to `has`:

````
const has = (thing) => {
   
    return (datum) => {
        return datum.includes(thing);
    }
};

dataset
    .filter(has(Z))
    .map(transformToY)
    .some(isZ);
````

By the way, this method in its more general sense [3] is called partial application currying, a technique named after the mathematician Haskell Curry. Haskell was named after him as well, and in Haskell, functions, as a matter of course, curry their values. Currying is a technique for evaluating function arguments where, instead of passing all of the arguments you have into a single function, you call a function on one argument and receive a new function that accepts the next one, which returns a new function that accepts the next one, and so on, until there are no more arguments left and a value is returned. That's right, I tricked you into learning what currying was! The benefit, as we can see, is that your function becomes more flexible, independent of outer context and globals, and more expressive if you use it in the right context. 

[0] Technically, the first arg to hasX is in its execution context, the second depends on the type, and third is from an outer context?

[1]

[2]
