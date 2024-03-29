# Sorting a List of Tuples


Here's a list of tuples:

<pre>
<code class="language-python">mylist = [ (0, 'z'), (0,'n'), (0,'a') ]
</code></pre>

If we sort this list with `sorted`, 

<pre>
<code class="language-python">print sorted(mylist)
# prints [(0, 'a'), (0, 'n'), (0, 'z')]
</code></pre>


Python will compare the first item in each and if there is a tie, move on to the second.  If there is a tie in the second case, (and we provide no additional ways to sort), there is no more sort criteria.  So in a tie, the items are sorted in the order in which they appeared in the original list. This extra specification is an attribute of a sort algorithm known as stability, and Python's `sorted` algorithm proceeds this way.

The zeros tied, so the secondary keys 'z', 'n' and 'a' were compared to determine the order of the sorted `mylist`.


It is useful to think of sorting as the transformation of each value from the original sequence into something that can be compared using the relations "less than", "equal" and "greater than".  The output of the sort is the original values but in the order of the transformed set.
    
Here's some code and then a mental reconstruction of it:

<pre><code class="language-python">
animals = ['bird','aardvark','lemur','grasshopper']
print sorted(animals)

# ['aardvark', 'bird', 'grasshopper', 'lemur']

# code to print out our mental concept

# def trfm(word):
#   l = ( ord(i) for i in word )
#   return ', '.join( str(a) for a in l)

# print animal.ljust(20), ' '.join( tuple('{:3}'.format(i)

# for animal in animals:
#   print animal.ljust(20), ' '.join( tuple('{:3}'.format(i)
#                                             for i in trfm(animal)
#                                          )
#                                   ) 
 
words as letters         corresponding ascii values 
---------------          --------------------------
'b i r d'                98  105 114 100
'a a r d v a r k'        97  97  114 100 118 97  114 107
'l e m u r'              108 101 109 117 114
'g r a s s h o p p e r'  103 114 97  115 115 104 111 112 112 101 114
'a l l i g a t o r'      97  108 108 105 103 97  116 111 114




original sequence       sorted sequences 

7                       2 1 0
2                       4 1 0
4                       5 0 1
5                       7 0 1</code></pre>



Functions that could produce the sorted sequences are:
 
<pre><code class="language-python">
    # default case 
    sorted 

    def is_even(n):
      return n%2
</code></pre>

This happens with even the default `sorted`.  Using the `key` parameter is merely specifying an additional one in the case of a tie.  The default sort involves one algorithm and the `key` sort is providing another.  

When comparing 'alpha' and 'zebra', this might be a sketch of the internal representation of what's going on:

(97, 108, 112, 104, 97, 122) -> alpha_a
(110, 108, 112, 104, 97, 122) -> alpha_n
(122, 108, 112, 104, 97, 115) -> alpha_z 

In the case of 'alphaz' and 'alphas' above, the items are compared one element at a time until one of their elements differ, at which point the original value to which the smaller one belongs is inserted first into the final sorted list (assuming we are using the default 'ascending' order).



# Sorting with one or more Custom Functions 

The examples above didn't involve using a custom function, so let's do that.  We could write a redundant function that gets the same exact results that sorted gets by default:

<pre><code class="language-python">def custom(item):
    return item
</code></pre>

This is useless right? Well, no. It's great, because we can generate the same default sorted behavior ourselves.  When would this be appropriate? 

<pre><code class="language-python">def custom(item):
    return len(item), item
</code></pre>

What if we wanted to sort by length, but if two items have the same length, sort them by alphabetical order.  What we want to make use of is the 'fallback' logic above where the next element is compared in the case of a tie.  Let's write a custom function that produces two values, not just one.  This way, the transformed values are tuples and are compared in the same way that mylist above is compared. There are no parenthesis in the return statement from custom, but understand that it's returning a tuple containing first the integer length of the word and second, a tuple of ascii values that represent each letter in the word. 

Here's my conceptual representation of what python is doing:

( 6, (97, 108, 112, 104, 97, 122) ) -> alphaz

( 6, (97, 108, 112, 104, 97, 115) ) -> alphas



Here's a sort to show the end result conforms with the representation above.

<pre><code class="language-python">print sorted(['alphaz','alphas','mint','mine'] ,key=custom)

['mine', 'mint', 'alphas', 'alphaz']
</code></pre>

