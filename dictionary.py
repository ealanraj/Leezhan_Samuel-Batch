# #dictionary
# #A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# #syntax:
# 'dictionary = {key1 : value1, key2 : value2}'

# d = {"name": "Leezhan","place": "pondicherry"}

# #key should be immutable

# #keys
# print(d)
# print(d["name"])
# print(d["place"])

# #duplicates not allowed
# d2 = {"name":"alanraj","name":"leezhan"}#recent key will be updated
# print(d2)

# #changable
# print(f"before : {d}")
# d["place"] = "cuddalore"
# print(f"after : {d}")

# #len
# print(len(d))#one key:value pair will be considered as one item


# #values can be of any datatype

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict)

# #type
# print(type(thisdict))

# #constructor - dict()
# d3 = dict(name = "alan", place = "pondicherry", course = "python")
# print(d3)

# d4 = dict([("name","alan"),("place","pondicherry")])#can pass list of tuple
# #must contain only two values in each tuple(i.e, key and value)
# print(d4)


# print(dict((["name","alan"],["place","pondicherry"])))#can also pass tuple of lists


# #.get
# print(d)
# print(d.get("name"))
# print(d.get("course"))#if key not found, get method won't throw error
# ##print(d["course"]) #KeyError:

# #keys - return list of keys
# print(d.keys())

# #.values()
# print(d.values())

# #add new item
# d["course"] = "python"#will create a new key:value pair
# print(d)

# #.items() - tuples in a list
# print(d.items())

# #in loop (access keys)
# print(d.keys())
# for i in d:
#     print(i)
# #check if key exists

# if "name" in d: #default - iterate through keys
#     print(True)
# else:
#     print(False)

# #if you want to iterate through values
# for i in d.values():
#     print(i)
# print("*"*40)
# #keys

# for i in d.keys():
#     print(i)
# print("*"*40)

# for i in d.items():
#     print(i)

# #using range

# for i in d:
#     print(d[i])

d = {"name" : "alanraj", "age": 22, "place": "pondicherry"}
# print("before",d)

d1 = d.copy()
d1["place"] = "lawspet"
# print("d1",d1)
# print("d",d)

#Nested Dictionary
# Syntax: dict = {"key1":{"key1":"value1"}, "key2":{"key2":"value"}}
myfamily = {
            "child1" : {"name" : "Emil","DOB" : 2004},
            "child2" : {"name" : "Tobias","DOB" : 2007},
            "child3" : {"name" : "Linus","DOB" : 2011}
            }
print(myfamily["child1"])
print(myfamily["child2"])
print(myfamily["child3"])

#access nested dictionary
print(myfamily['child1']['name'])
print(myfamily['child1']['DOB'])

#accessing nested dictionary in loop
for key,value in myfamily.items():
    print(key,value)
    for i in value:
        print(i,value[i])



#popitem - removes last inserted item
myfamily.popitem()
print(myfamily)

#from keys - create a dictionary with different keys and same values
keys = ["A","B","C"]
d = dict.fromkeys(keys,"Alive")
print(d)

d1 = dict.fromkeys(keys) #default value None
print(d1)

d = {"name":"alanraj","age":22}
d.setdefault("name","leezhan") #if key exists, the value remains same, if key dosen't exist it will insert a new item
print(d)
d.setdefault("place","Pondicherry")#this inserts a new item
print(d)

#UPDATE

d.update({"name":"Leezhan"})
print(d)


















