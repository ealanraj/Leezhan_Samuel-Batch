#Tuple
tup = (1,2,3,4,5)
print(tup)
print(type(tup))

#A tuple is a collection which is ordered and unchangeable

#immutable datatype
##Tuple items are ordered, unchangeable, and allow duplicate values.

#indexing
print("index 0 :",tup[0])
#slicing
print("sliced indices [2:]",tup[2:])

#unchangable
##tup[0] = 2
##TypeError: 'tuple' object does not support item assignment

#allow duplicated
tup2 = tuple(chr(i) for i in range(97,104))#comprehension
print(tup2)

tup3 = ("a","a","a")#allows duplicates
print(tup3)

#len
print(len(tup3))


#create tuple with single item
tup_s = ("a",)
print(tup_s)


#ALLOWS ALL DATA TYPES
tup4 = (1,2,3,"a","b","c",True,False,[1,2,3],("a","b","c"))
print(tup4)


#check if item exists

if [1,2,3] in tup4:
    print("yes, '[1,2,3]' exists in the tuple")
else:
    print("No, '[1,2,3]' does not exist in the tuple")

print("a" in tup4)

#change the items of tuple by converting into a list
tup5 = (1,2,3)
print(f"Tuple before: {tup5}")
l = list(tup5)
l.append(4)
tup5 = tuple(l)
print(f"Tuple after: {tup5}")

#concatenation of tuples
tup6 = ("apple",)
tup5+=tup6 #tup5 = tup5 + tup6
print(f"tup5 + tup6 : {tup5}")

#del keyword - to delete
del tup6
##print(tup6)#NameError: name 'tup6' is not defined. Did you mean: 'tup'?

#unpack
fruits = ("apple", "banana", "cherry")
## a,b = fruits        #ValueError: too many values to unpack (expected 2)
a,b,c = fruits
print(f'''a => {a}
b => {b}
c => {c}''')

# assign multiple values to the variable using *
a,*b = fruits
print(f'''a => {a}
*b => {b}''')

#for loop
for i in tup5:
    print(i)

#loop through the index
print("\nFor Loop")
for i in range(len(tup5)):
    print(f"index : {i}, value : {tup5[i]}")

print()
print("While Loop")
#while loop
i = 0
while i < len(tup5):
    print(f"index : {i}, value : {tup5[i]}")
    i+=1

#multiply tuples
print("Multiply Tuples")

print("tup5 * 2 :",tup5*2)

#count
print("\nCount Method\n")
print("tup5.count('apple'):",tup5.count("apple"))

#index
print("\nIndex Method\n-----------------------")
print("tup5 :",tup5)
print("tup5.index('apple') :",tup5.index("apple"))

#nested tuple - tuple inside a tuple
print("\nNested Tuple\n------------------")
t = (1,2,3,("a","b","c"))
print(t)
#to access the nested tuple
print("t[-1][1] :",t[-1][1])

#sorted function
l = (3,2,1)
sorted(l)
[1, 2, 3]
sorted(l,reverse=True)
[3, 2, 1]












