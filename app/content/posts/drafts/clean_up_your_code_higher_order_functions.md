Functional methods like `map`, `filter`, `reduce`, `some` and `all` can bring clarity and brevity to the parts of your code that transform data.

Below, I'm sending data through a series of functional methods that call a named callback on each item in the array it receives. See how clear it can be?

    dataset
        .filter(hasX)
        .map(transformToY)
        .filter(compact)
        .length;

Without modifying the original dataset, this would tell me the number of elements that fit some specific criteria (it has `X`, and when you transform it to you, it's still truthy).

This code is clear enough, but it's still a fairly rigid exchange. Filter's callback can only work on a single input that filter hands to it. Let's imagine that the `X` in `hasX` or the `Y` in `transformToY` could be parameterized. Then we could separate the property-checking code from the property-specificying code. But right now, everything `hasX` uses to do its work is contained within its lexical definition. How can we parameterize `X` ? 

## Closure 

Well, a first step would be to simply refer to an outer parameter from within the `hasX` function definition. Like this:

    const thing = 'init';
    // ... code ...
    const hasX = (datum) => datum.includes(x);

It uses closure to refer to an x from an outer scope. This isn't any good, though. Here's why:

+ Legibility: When you look at the `hasX` definition, the only thing that's clear about where `x` comes from is ... somewhere else. This means you have to go looking for it. We want to avoid this sort of cognitive noise. 
+ Flexibility: We still don't have any greater control over the property-specifying code, since `X` is effectively still hard-coded into the functon. 
+ Portability: `hasX` is like your difficult friend `Y`.  You can't just take him *anywhere* because he's always going on about something that no one's ever heard of and he prefers it that way.
+ Testability: I'd like to drop `hasX` off at my test suite, but the value to which `thing` refers is lexically scoped, so if I export the function from a module, I have to make sure that the satellite datum, `x`, is in that module.

## Temporality, Execution Context

So let's make `hasX` a truly great, capable, adaptable citizen in our code. If we think about the order of events in our functional pipeline, `hasX` returns a value at a single point in time.  But if we break the compound work that it does into two separate functions, we can achieve greater control over the timing of their evaluations and where their input comes from.

We'll still need the technique of closure, but we can totally eliminate the lexical distance between the value closed over by putting one of our two functions inside of the other. Which one comes first?

Let's think about a function returning a function for a second and just get clear on the temporality of this technique:

    fnA(x) {

        return fnB(y) {
            return x.method(y); 
        }

    }

I hope it is not a surprise to you that you will need to call `fnA` before you can call `fnB`. We could call these two functions like this:

    fnA(2)(3);

or like this:

    fnA(3)(2);

The order would depend on the actual thing you need to get done. Let's try this out with our `hasX` function, which we'll be calling `has` from now on:

    const has = (x) => {
        return (datum) => {
            return datum.includes(x);
        }
    };

Note that I'm using anonymous functions here because it keeps the names introduced into the program to a minimum. Since from the calling standpoint you only really need to name that outermost function, it's not any benefit to you to name the inner function. 

Also, you could define this function with fewer characters if you want to make the most out of the ES6 syntax:

    const has = (x) => (datum) => datum.includes(x); 

This definition syntax is pretty much infinite, so if you wanted to, you could write a function that returns a function that returns a function:

    const fn1 = (a) => (b) => (c) => max(a, b, c);

And now, when you get around to using `has`, you can write this:

    dataset
        .filter(hasX('Z'))
        .map(transformToY)
        .some(isZ);

That is clean af! And why don't we, in good aesthetic taste, rename the function to `has`:

    const has = (thing) => {
       
        return (datum) => {
            return datum.includes(thing);
        }
    };

    dataset
        .filter(has(Z))
        .map(transformToY)
        .some(isZ);


Conclusions:

- can make your code much more readable
- a special, limited case of currying
- avoid globals

By the way, this method in its more general sense [3] is called partial application currying, a technique named after the mathematician Haskell Curry. Haskell was named after him as well, and in Haskell, functions, as a matter of course, curry their values. Currying is a technique for evaluating function arguments where, instead of passing all of the arguments you have into a single function, you call a function on one argument and receive a new function that accepts the next one, which returns a new function that accepts the next one, and so on, until there are no more arguments left and a value is returned. That's right, I tricked you into learning what currying was! The benefit, as we can see, is that your function becomes more flexible, independent of outer context and globals, and more expressive if you use it in the right context. 


[0] Technically, the first arg to hasX is in its execution context, the second depends on the type, and third is from an outer context?

[1]

[2]
