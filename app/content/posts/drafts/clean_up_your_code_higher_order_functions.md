In JavaScript, functional array methods like `map`, `filter`, `reduce`, `some` and `every` can bring a lot of clarity and brevity to the parts of your code that transform data.  

Here's an example of what I mean:

    dataset
        .filter(hasX)
        .map(toY)
        .filter(compact)
        .length;

I've filtered a dataset down to the subset where each item has X, turned each item of the resulting subset into a Y, kept only the truthy values, and counted the length of the final array. The original dataset isn't affected by this transformation because each of these methods produces a copy of its input.

There are two major things going on here that make this approach work. There is the design-level notion of uniformity where each step takes an array as input and returns an array, and the callback passed to each step works with a single item of the input array.  And there is the naming strategy. Each callback has a name consistent with the nature of the method that invokes it. The `filter` callback name is a proposition that can be true or false. The name of the `map` callback indicates that the item is being transformed to something elese. Finally, these methods (unlike, say `sort`) are immutable methods that produce a copy of their input and return their data so that it can be used in a chained format.

This code is clear enough, but it's still a fairly rigid exchange: `filter`'s callback can only work on a single input that filter hands to it. Let's imagine that the `X` in `hasX` or the `Y` in `transformToY` could be parameterized. Then we could separate the property-checking code from the property-specificying code. But right now, everything `hasX` uses to do its work is contained within its lexical definition. How can we parameterize `X` A first step would be to simply refer to an outer parameter from within the `hasX` function definition. Like this:

    const x = 'init';
    // ... code ...
    const hasX = (datum) => datum.includes(x);

It takes advantage of scoping rules to refer to an x from another location in the code. This isn't any good, though, and here's why: When you look at the `hasX` definition, the only thing that's clear about where `x` comes from is ... somewhere else. If we can parameterize x, we can skip having to go look for it entirely. And we still don't have any greater control over the property-specifying code, since `X` is effectively still hard-coded into the functon. 

## Temporality, Execution Context

So let's make `hasX` a truly great, capable, adaptable citizen in our code. If we think about the order of events in our functional pipeline, `hasX` returns a value at a single point in time.  But if we break the compound work that it does into two separate functions, we can achieve greater control over the timing of their evaluations and where their input comes from. 

We'll still need to take advantage of scope, but we can virtually eliminate the lexical distance between the value closed over by putting one of our two functions inside of the other. But which one comes first?

Let's think about a function returning a function for a second and just get clear on the temporality in this technique:

    fnA(x) {
        return fnB(y) {
            return x.method(y); 
        }
    }

I hope it is not a surprise to you that you will need to call `fnA` before you can call `fnB`. We could call these two functions like this:

    fnA(2)(3);

or like this:

    fnA(3)(2);

The order would depend on the actual thing you need to get done. Let's try this out with our `hasX` function, which we'll be calling `has` from now on. Since we need to ultimately pass this function to `filter`, it needs to return a function that accepts a piece of data from the pipeline. If we start with the function that `filter` will apply to the dataset, we can reason backward to the definition of the compound function. 

    const hasX (datum) => datum.includes(x);

We now need to wrap this in an outer function that returns this function when called:

    const has = (x) => (datum) => datum.includes(x);

And finally, we can use it like this:

    dataset
        .filter(has('a'))
        .map(transformTo('b'))
        .filter(compact)
        .length();


## A Real Example

Imagine I have a list of filenames that have a name and a date:

    alice_2016-12-07.json
    alice_2016-12-04.json
    alice_2016-12-09.json
    alice_2016-12-01.json
    alice_2016-12-03.json
    alice_2016-12-11.json
    bob_2016-12-03.json
    bob_2016-12-09.json
    bob_2016-12-02.json
    ...

And let's say I want to find any files for any person in a list for whom there is missing data in some date range. Let's say the date range is '2016-12-01' through '2016-12-15' and it is inclusive. And let's say that the names I care about are 'bob','alice', and 'fred'. Here's how I could use this technique (which is a limited case of currying by the way):

    const moment = require('moment');
    const filenames = [

        'alice_2016-12-07.json',
        'alice_2016-12-04.json',
        'alice_2016-12-09.json',
        'alice_2016-12-01.json',
        'alice_2016-12-03.json'
        'alice_2016-12-11.json'
        'bob_2016-12-03.json',
        'bob_2016-12-09.json',
        'bob_2016-12-02.json'

    ];

    const inRange = (start, stop) => (date) => moment(date).isBetween(moment(start),moment(stop));

    filenames
        .filter()

I should note that I'm using ES6 syntax to express this in a much more concise manner.  It may not always be more readable to use ES6 syntax, so please don't consider it a silver bullet. But in this case I find it makes the code concise yet readable. This would be the ES5 alternative:

    function inRange (start, stop) {
        return function (date) {
            return moment(date).isBetween(moment(start), moment(stop));
        }
    }

This definition syntax is generalizable, so if you wanted to, you could write a function that returns a function that returns a function:

    const fn1 = (a) => (b) => (c) => max(a, b, c);

And now, when you get around to using `has`, you can write this:

    dataset
        .filter(hasX('Z'))
        .map(toY)
        .some(isZ);

## A Real Example

    const moment = require('moment');
    const assert = require('assert');
    const users = [ 'alice', 'bob', 'fred' ];
    const filenames = [ 

        'alice_2016-12-07.json',
        'alice_2016-12-04.json',
        'alice_2016-12-09.json',
        'alice_2016-12-01.json',
        'alice_2016-12-03.json',
        'alice_2016-12-11.json',
        'alice_2016-12-31.json',
        'bob_2016-12-03.json',
        'bob_2016-12-09.json',
        'bob_2016-12-02.json'

    ];

    const range = (max) => [ ...Array(max).keys() ];
    const parseDateString = (filename) => filename.split('_')[1].split('.')[0];
    const belongsTo = (user) => (filename) => filename.split('_')[0] === user;
    const inDateRange = (start, stop) => (dateString) => moment(dateString).isBetween(moment(start), moment(stop), null, '[]');
    const generateDateRange = (start, stop) => {

        let [ startDate, stopDate ] = [ moment(start), moment(stop) ];
        let diff = moment.duration(stopDate.diff(startDate)).days();

        return range(diff + 1).map(offset => startDate.clone().add({ days: offset }).format('YYYY-MM-DD'));
        
    };
    const getMissingDates = (user, filenames, { start, stop }) => {

        const idealDates = generateDateRange(start, stop);

        const userFilesInRange = filenames
            .filter( belongsTo(user) )
            .filter( filename => inDateRange(start, stop)(parseDateString(filename)) );

        return idealDates
            .filter(idealDate => !userFilesInRange.map(parseDateString).includes(idealDate));

    };
    const missingDataReport = (users, filenames, dateRange) => {

        const reportSchema = {
            dateRange: null,
            users: {}
        };

        console.log();

        const run = () => { 

            let data = users.reduce((obj, user) => {

                obj['dateRange'] = dateRange; 
                obj['users'][user] = { 
                    'missingDates': getMissingDates(user, filenames, dateRange),
                    'files': filenames.filter(belongsTo(user))
                };

                return obj;

            }, reportSchema);

            return data;

        };

        return { run };

    };

    const data = missingDataReport(users, filenames, { start: '2016-12-01', stop: '2016-12-15' }).run();
    console.log(JSON.stringify(data, null, 2));

