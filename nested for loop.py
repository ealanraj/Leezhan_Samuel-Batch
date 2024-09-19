##for i in range(1,6):#outer loop
##    print(i,"Table")
##    print("-"*10)
##    for j in range(1,11):#inner loop
##        print(f"{i} x {j} = {i*j}")
##    print("*"*50)

#loop in reverse:-

##for i in range(5,0,-1):
##    print(i)


##for i in range(5):
##    for j in range(5):
##        for k in range(5):
##            print(i,j,k)

##
##for i in range(1, 6):
##    for j in range(1, i + 1):
##        print("*", end=" ")
##    print()
##    for k in range(1,j+2):
##        print("*", end=" ")
##        
##    print()  # Move to the next line after each row



#While Loop

#syntax
'''
    while <condition>:
        <block of code to be executed until the condition is True>
'''

##i = 0
##while i<=5:
##    print(i)
##    if i==1:
##        print(i,"if")
##        i+=1
##    else:
##        print(i,"else")
##        i+=1


i = 1
##while i<6:
##    i+=1
##    j=1
##    while j<6:
##        print(j)
##    j+=1
##    print()



#control Statements:-

##
###While Loop
##i = 1
##while i<=10:
##    print(i)
##    i+=1
##print()
###Nested While Loops
##i = 1
##while i<=5:
##    j = 1
##    while j <=5:
##        print(i,j)
##        j+=1
##    print()
##    i+=1
##    
###control statements
#break - stops the loop
#continue - skips the iteration loop
#pass - used for future purpose (passes to the next iteration!)

number = 0
while number <20:
    number += 1
    if number==10:
        pass
    elif number % 2 == 0:
        print(number,"even")
    else:
        print(number,"odd")
