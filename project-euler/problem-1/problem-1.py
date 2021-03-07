"""
Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 of 5 below 1000
"""

#Method 1: First thoughts -- Go through each value below 1000, see if they are a multiple of 3 or 5, add to list and sum

below_100 = []
for x in range (1,1000):
    if x%3 == 0 or x%5 == 0:
        below_100.append(x)
print("Method 1 solution: " + str(sum(below_100)))

#Method 2: Shorter?

print("Method 2 solution: " + str(sum(set([x for x in range(1,1000) if x%5 == 0] + [y for y in range(1,1000) if y%3 == 0]))))

"""
Notes from Tim:
    - Map: Apply some kind of transformation to every element of a list
    - Filter: Filter out some valeus
    - Reduce: Combine values in some way

Functional programming: Computations are done by combining functions that take arguments and return a concrete value (or values) as a result. These functions don't modify their input arguments and don't change the program's state. They just provide the result of a given computation.

Since map() is written in C and is highly optimizd, its internal implied loop can be more efficient than a regular python for loop.

Second advantage of using map() is related to memory consumption. WIth a for loop, you need to store the whole list in your system's memory. With map(), you get items on demand, and only one item is in your system's memory at a given time.


In python 2, map() returns a list.
In python 3, map() returns a map object -> You'll need to convert it to a list.

lambda functions are handy when you need to pass an expression-based function to map().

You can actually use multiple iterables with a function in map as long as your function can take two variables

filter() is a built-in function that takes two positional arguments: function that yields true or false and an interable.
filter() takes an iterable and filters out values based on a predicate or boolean-valued function.

reduce() is in module functools
reduce() is useful when you need to apply a function to an iterable and reduce it to a single or cumulative value (reduction or folding)
"""

#Method 3: Functional one line

import functools, operator

print("Method 3: " + str(functools.reduce(operator.add, filter(lambda x: not (x%3 and x%5), range(1,1000)))))


