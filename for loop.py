### For Loop:-
##
##for i in [1,2,3]:#iterator
##    print(i)
##
##fruits = ["apple", "banana", "cherry"]
##
##'''
##
##1st iteration - x = "apple"
##2st iteration - x = "banana"
##3st iteration - x = "cherry"
##'''
##
##for x in fruits:
##  print(x)
##
##print("-"*50)
##for i in "ocean academy":
##    print(i)
##print("-"*50)
###range function
##    #syntax: range(start (inclusive), stop (exclusive) , step)
##for i in range(0,10+1):
##    print(i)
##print("-"*50)
##for i in range(0,11,2):#even
##    print(i)
##print("-"*50)
##for i in range(1,11,2):#odd
##    print(i)
##print("-"*50)
##for i in range(10):#if we pass a single value inside the function, it will be considered as stop value
##    print(i)
##print("-"*50)
###else in for loop
##
##for i in range(1,6):
##    print(i)
##else:
##    print("The loop has ended")
##print("-"*50)
##
##for i in range(5):
##    print(i,"hello")
##
##print("-"*50)
##for _ in range(5):
##    print("hello world")
##
##n = int(input("which multiple do you want to see?"))
##for i in range(1,6):
##    print(n,"x",i,"=",i*n)

s = "applesdfghjkl"
result = 0

for i in s:
    result+=1
    
print(result)


l = [1,2,3]
result = 0
for i in l:
    result+=i
    print(result)

###iteration:-
##
###i = 1
##    result+=1
##    print(result)
###i = 2
##    result+=2
##    print(result)
###i = 3
##    result+=3
##    print(result)
##    
###loop ended







