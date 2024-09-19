#set
#immutable datatype
#unordered, unchangable*, doesn't allow duplicates
##* Note: Set items are unchangeable, but you can remove items and add new items.

s = {1,2,3,3}#No duplicates
print(s)

#True - 1
#False - 0

s1 = {1,0,True,False}
print(s1)

#len
print(len(s1))


#datatypes allowed - string, int, boolean, tuple, float

##s2 = {1,2,[1,2,3]} #TypeError: unhashable type list (changable datatype)
##print(s2)

s2 = {1,2,3,"a","b",True,False,(1,2,3,4)}
print(s2)


#set constructor

l = [1,2,3,1,2,3,4,4,5,5,6,6,7,7,8,8]
print(set(l))#converts into set and removes duplicates

#access items using loop

for i in s2:
    print(i)

#check item exists

print(1 in s2)
print(1 not in s2)


#method

#.add()

print(s)
s.add(4)
print(s)

#.update() - used to add items from any iterable
#similar to extend method in list

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

thisset.update(s)#any iterable
print(thisset)

#.remove() - removes item

thisset.remove("apple")
print(thisset)
##thisset.remove("abc")#KeyError:
#will raise error if item does not exists

#.discard() - to remove items but it won't raise an error if item dosen't exist

thisset.discard("abc")
thisset.discard("banana")
print(thisset)

#.pop() - randomly removes an item from the set
print(thisset.pop())
print(thisset)

#.clear() - clears all items and returns empty set

thisset.clear()
print(thisset)
#empty set - set()

#del - keyword deletes the entire set


#union or |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

result = set1.union(set2)#method
print(result)
print(set1|set2)#operator


#union multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

result = set1.union(set2, set3, set4)
print(result)
print(set1|set2|set3|set4)#can be used only on sets

#join set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

result = x.union(y)
print(result)

#intersection - &

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.intersection(set2))
print(set1 & set2)

#intersection_update - will update the original set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)#changed the original set1


# difference() or -
#- will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

result_set1 = set1.difference(set2)
result_set2 = set2.difference(set1)
print(result_set1)
print(result_set2)

print(set1 - set2)

#difference_update()
set1.difference_update(set2)
print(set1)


#symmetric_difference() or ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
print(set1 ^ set2)

#symmetric_difference_update() - will change the first set

set1.symmetric_difference_update(set2)
print(set1)

##isdisjoint() - Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

result = x.isdisjoint(y) 

print(result)

#issubset - Returns whether another set contains this set or not

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
print(x<=y)

#issuperset - contains another set inside it
print(x.issuperset(y))
print(y.issuperset(x))
print(y>=x)



















