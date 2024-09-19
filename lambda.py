# # Syntax: lambda arguments : expression
# sq = lambda x : x**2
# print("sq",sq(8))
# add = lambda x,y : x+y
# print("add",add(5,10))

# multiply = lambda x,y :x*y
# print("multiply",multiply(5,5))

# #getting input from user and calling the function!
# x = int(input("x: "))
# y = int(input("y: "))
# print("multiply",multiply(x,y))

# #lambda inside another function

# def func(n):
#     return lambda x : x*n

# double = func(2)
# print(double(2))
# triple = func(3)
# print(triple(3))


l = lambda x, y = 2 : x*y #default argument

print(l(2,5))
print(l(2))

#get multiple arguments from the user

add = lambda *x : sum(x)
print(add(1,2,3,4,5,6,7,8,9))