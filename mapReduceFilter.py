add = lambda x,y : x+y
print(add(5,5))

# function(parameter = argument)
# for example: print(end = "\n")

'lambda function can be passed as arguments'

d = {"a":2,"b":3, "c":1}

l = ["akjgf","dfdfd","as","df","ghe"]
ans = sorted(l,key=len)
print(ans)

result = dict(sorted(d.items(),key= lambda x : x[1]))
print(result)

#map Reduce Filter
'1. Map'
# map takes one argument
# Syntax: map(function, iterator)
# function will be applied to each and every item of the iterator.

l = [2,3,4,5,6]

sq = lambda x : x**2
cube = lambda x : x**3

squared_items = list(map(sq,l))
cubed_items = list(map(cube,l))

print(squared_items)
print(cubed_items)

'2. Reduce'
#reduce function is located in functools module
# reduce takes two positional arguments
import functools #import the module

l = [10,10,10,10,10]
add = lambda x,y : x+y
print(functools.reduce(add,l))
print(functools.reduce(lambda x,y : x*y, l))

'3. filter' #affects the number of items
#returns as iterator
#can be converted using constructors

l = [1,2,3,4,5,6,7,8,9,10]

isEven = lambda x : x%2==0
isOdd = lambda x : x%2!=0

evenResult = list(filter(isEven, l))
oddResult = list(filter(isOdd,  l))
print(evenResult)
print(oddResult)

'4. accumulate'
# Syntax: itertools.accumulate(iterable, func=operator.add)

import itertools
l = [10,10,10,10]
print(list(itertools.accumulate(l))) #default function = addition

sub = lambda x,y : x-y
print(list(itertools.accumulate(l,sub))) #gives cummulative value for all items
# print(functools.reduce(l)) # only accumulate accepts one arguments


print(list(map(lambda x: 'even' if x%2==0 else "odd", [1,2,3,4,5,6,7,8,9])))





