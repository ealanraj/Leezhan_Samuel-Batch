from module import *
import itertools
import functools

from functools import reduce
from itertools import * # import all functions


l = [1,2,3,4,5]
print(list(map(sq,l)))
print(reduce(add,l))
print(list(accumulate(l,add)))

print(tup)
print(d)

import itertools as it # re-naming a module using as keyword
print(list(it.accumulate(l,add)))
import module
print(dir(module))
print(greet.__doc__)

import datetime

x = datetime.datetime.now()

print(x)
'''
These are in-built math functions
min()
max()
abs()
pow()'''

# now, we will use math module for advanced functions

import math

print(math.pi)
print(math.sqrt(64))

print(math.ceil(5.6))#return the highest possible integer
print(math.floor(5.6))#return the least possible integer
print(dir(math))
print(math.factorial(5))

