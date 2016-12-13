If you're familiar with Mr. Show, you may know the technique common to many of their most successful sketches: assiduous repetition of a single idea. It's the key to 'The Story of Everest' and 'The Audition', where the same thing happens again and again, and things gets exponentially funnier.

The sketch <a href="https://www.youtube.com/watch?v=cGuT97v4pv0">'Change for a Dollar'</a> uses this tight repetition to play a good joke on the fate of value in the hands of pure bureaucracy. Oddly, the structure is legimately recursive and I think serves as a good (if not highly alternative) illustration of the winding-and-unwinding process of a recursive program.

![Mr. Show's Bob and David](https://i.vimeocdn.com/video/199532043_640.jpg)

The gist of the sketch is that a man asks a convenience store clerk to exchange a dollar for four quarters. Instead of just saying yes or no, the clerk, after some delay, has to ask his boss for permission, and it turns out his boss must also, after some delay, ask *his* boss for permission. This continues until the original request reaches an employee with the credentials to say yes or no. At that point, the answer propagates back through each boss to the requesting underling. When that underling is the store clerk, he can tell the customer the answer.
 
In terms related to recursion, each scene is the execution context of a new function placed on top of the call stack that stores the state of this `change_for_a_dollar` program. If the arguments to the function are `employee` and `boss`, then at the end of the function call, we call the function again with `employee.boss` and  In each scene, the employee seeks authorization from his boss to make change for a dollar. If the employee's boss isn't able to authorize, he has to call *his* boss.

Below, I've created a basic model to represent the chain of command in this haplessly bureaucratic corporation (notice that employee5 is the only one who has the `authorize` method, meaning only he can sign off on the 'change for a dollar' request): 

%CODE%

The five employee objects make up a singly-linked-list where each employee save the last has a reference to his boss, who has a reference to his boss, etc. We can use this structure to recurse through the list until an employee with an `authorize` method is found.

%CODE%

When the `authorize` method is found on an employee, the results of that method call are returned. This is our base case, and causes each function on the call stack to resolve its return value until the original caller is reached. 

%CODE%

Why is this not iterative?

Just in case you were wondering why I'm making a big deal about this being a good example of recursion instead of iteration using a while loop, there are two reasons:

  1. The context for each authorization check is a totally new location relative to the specific employee and boss involved. If the sketch demonstrated iteration (like 'Story of Everest' and 'The Audition' mentioned above), the context of the employee traversal process would be the `customer.getChangeForADollar` method throughout, aka, the whole sketch would have to take place in the convenience store. 
  2. The sketch demonstrates an explicit 'unwinding' phase where the ultimate answer is relayed from the top of the command-chain, through each boss and underling, to the caller and in exactly the reverse order of the recursive calls. I'd go so far as to say that this unwinding phase contains the punchline of the joke.  

All of this is just to demonstrate that while a *good* joke may use repetition, it is the rare comedic gem that implements it recursively! In any case, I'm sure that my analysis eventually breaks down, so if **YOU** are interested in telling me exactly where it does, I would be flattered. You can call me on my twitterphone, the number is simply: <a href="https://twitter.com/drlolzrofl">@drlolzrofl</a>. 

[note: there are almost exclusively gendered pronouns in this post and the reason is simply that the relevant roles in the sketch are played by David Cross and Bob Odenkirk, who in fact play all of the employees and bosses.]
