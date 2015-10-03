CHANGE FOR A DOLLAR

While the Mr. Show sketch 'Change for a Dollar' seems to be a joke on the fate of value in the hands of pure beaurocracy, it also demonstrates the winding and unwinding of function calls in a recursive operation quite nicely.

If you've seen at least a few of Mr. Show sketches, then you know that a large part of the comedy depends on assiduous repetition of a narrow concept.  However, 'Change for a Dollar' goes beyond that in using the same structure  

The gist of the sketch is that a man asks a grocery store clerk to exchange a dollar for four quarters. Instead of just saying yes or no, the clerk has to ask his boss for permission, and it turns out his boss must in turn ask his boss for permission, and so on until the original request reaches an employee with the credentials to say yes or no. At that point, the answer propagates back through each boss to his underling, until the answer reaches the context of the original requester where the employee can give the requester the answer.

Each scene in the sketch effectively operates as the execution context for a new function placed on top of the call stack. In each new scene, the boss from the previous scene takes on the roll of the employee seeking an answer from his boss.  

It's time for some code. Here is a data structure that could represent the chain of command in this haplessly bureaucratic corporation (notice that employee5 is the only one who has executive power, meaning only he can sign off on the 'change for a dollar' request): 

var corporation = {

  emp1: {
    name:'Store Clerk',
    boss: this.emp2,
    execPower: false,
  },
  emp2: {
    name:'Store Manager',
    boss: this.emp3,
    execPower: false,
  },
  emp3: {
    name:'Regional Manager',
    boss: this.emp4,
    execPower: false,
  },
  emp4: {
    name: 'Corporate Executive',
    boss: this.emp5,
    execPower: false,
  },
  emp5: {
    name: 'President of the United States',
    boss: null,
    execPower: true,
    changeForADollarPossible: function() {
      return 'no';
      // i'm sure Mr. Show would have this function separate from the actual act of doing the exchange
      // and i bet the exchange function would require another entirely separate recursive operation
    }
  },

};




function changeForDollar?(employee, boss) {
}
