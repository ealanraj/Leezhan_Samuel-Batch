#Collection Module
'''The collection Module in Python provides different types of containers. A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them. Some of the built-in containers are Tuple, List, Dictionary, etc.'''
'''
Table of Content:
1. Counters
2. OrderedDict
3. DefaultDict
4. ChainMap
5. NamedTuple
6. DeQue
7. UserDict
8. UserList
9. UserString
'''
import collections
#1. Counters

l = [1,1,1,2,2,3,3,3,3]

counter = collections.Counter(l)
print(counter)