## Mr. Show, 'Change For a Dollar' and Recursion

If you're familiar with Mr. Show, you probably know that a technique common to some of the funniest (and worst) sketches is the assiduous repetition of a single idea. This technique works beautifully in 'The Story of Everest' and 'The Audition', where the repetition continually heightens the comedic effect.

The sketch 'Change for a Dollar' uses this tight repetition to play a good joke on the fate of value in the hands of pure beaurocracy. Oddly, the structure is legimately recursive in nature and serves as a good (if not highly alternative) introduction to the winding-and-unwinding-process of a recursive routine.

Recursion? Mr. Show?

Yes, recursion! Yes, Mr. Show!

The gist of the sketch is that a man asks a convenience store clerk to exchange a dollar for four quarters. Instead of just saying yes or no, the clerk has to ask his boss for permission, and it turns out his boss must in turn ask *his* boss for permission, and so on, until the original request reaches an employee with the credentials to say yes or no. At that point, the answer propagates back through each boss to the requesting underling. When that underling is the store clerk, the customer receives the answer: 'no'.
 
You can think of each scene as the 'execution context' of a new function placed on top of the call stack created by the request to make change. For every scene, the boss from the previous scene assumes the roll of the employee seeking an answer from his boss. If the employee cannot authorize the request, he must call the same 'procedure' on his boss.      

Below, I've created a basic model to represent the chain of command in this haplessly bureaucratic corporation (notice that employee5 is the only one who has the `authorize` method, meaning only he can sign off on the 'change for a dollar' request): 

````javascript

var employee5 = {
  name: 'President of the United States',
  boss: null,
  authorize: function() {
    return 'no';
  }
};
var employee4 = {
  name: 'Corporate Executive',
  boss: employee5,
};
var employee3 = {
  name:'Regional Manager',
  boss: employee4,
};
var employee2 = {
  name:'Store Manager',
  boss: employee3,
};
var employee1 = {
  name:'Store Clerk',
  boss: employee2,
};

````

The five employee objects make up a singly-linked-list where each employee save the last has a reference to his boss, who has a reference to his boss, etc. We can use this structure to recurse through the list until an employee with an `authorize` method is found.

````javascript
var customer = {
  name: 'customer',
  say: function(phrase) { console.log(phrase)},
  getChangeForADollar: function(employee) {
    console.log('Asking the %s ...', employee.name);
    if (employee.authorize) {
      var answer = employee.authorize();
      return 'the answer is ' + answer +'.'; 
    }
    else {
      return this.getChangeForADollar(employee.boss);
    }
  }
};
````

When the `authorize` method is found on an employee, the results of that method call are returned. This is our base case, and causes each function on the call stack to resolve its return value until the original caller is reached. 

````
customer.say('I need change for a dollar.');
console.log(customer.getChangeForADollar(employee1));
````

Why is this not iterative?

Just in case you were wondering why I'm making a big deal about this being a good example of recursion instead of iteration using a while loop, there are two reasons:

  1. The context for each authorization check is a totally new location relative to the specific employee and boss involved. If the sketch demonstrated iteration (like 'Story of Everest' and 'The Audition' mentioned above), the context of the employee traversal process would be the `customer.getChangeForADollar` method throughout, aka, the whole sketch would have to take place in the convenience store. 
  2. The sketch demonstrates an explicit 'unwinding' phase where the ultimate answer is relayed from boss to underling in exactly the reverse order of the recursive calls. 

Note: the pronouns in this post are all male. The reason is simply that the relevant roles in the sketch are played by David Cross and Bob Odenkirk, who in fact play all of the employees and bosses.
