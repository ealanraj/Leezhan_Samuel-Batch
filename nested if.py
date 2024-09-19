# Nested if - else:-
'''
if condition1:
    # Code to execute if condition1 is True
    if condition2:
        # Code to execute if condition1 and condition2 are True
        if condition3:
            # Code to execute if condition1, condition2, and condition3 are True
            # ...and so on
        else:
            # Code to execute if condition1 and condition2 are True but condition3 is False
    else:
        # Code to execute if condition1 is True but condition2 is False
else:
    # Code to execute if condition1 is False
'''   
##
##m = int(input("please enter your mark to check grade: "))
##
##if m >= 90:
##    print("Grade A")
##    if m>=95:
##        print("excellent performance")
##    else:
##        print("wonderful performance")
##elif m>=75:
##    print("Grade B")
##    if m>=80:
##        print("Very Good")
##elif m>=65:
##    print("Grade C")
##    if m>=70:
##        print("Good")
##elif m>=45:
##    print("Grade D")
##    if m>=50:
##        print("fair")
##else:
##    print("Grade E")
##    if m<=35:
##        print("fail")
##
#####
##number = int(input("enter a number"))
##
##if number > 0:
##    print("The number is positive.")
##    if number % 2 == 0:
##        print("It's even.")
##    else:
##        print("It's odd.")
##elif number < 0:
##    print("The number is negative.")
##    if number % 2 == 0:
##        print("It's even.")
##    else:
##        print("It's odd.")
##else:
##    print("The number is zero.")


##

#match case
'''
match variable:
    case pattern1:
        # Code to execute if variable matches pattern1
    case pattern2:
        # Code to execute if variable matches pattern2
    case pattern3:
        # Code to execute if variable matches pattern3
    case _:
        # Default case, if no patterns match
'''

##n = input('''select any one option
##-> a
##-> b
##-> c
##: ''')
##
##match n:
##    case "a":
##        print("you've selected a")
##    case "b":
##        print("you've selected b")
##    case _:
##        print("you've selected c")



size = int(input('''
Welcome to our pizza shop!
Which type of pizza are you looking for?
Available options:
1. small
2. medium
3. large

enter value in number!
'''))

match size:
    case 1:
        cheese = input("you've selected small pizza, do you want cheese add-on? (yes/no)")
        if cheese == "yes":
            print("Okay, I have added!!")
            n = int(input("how many pizzas do you want?"))
            print("Your Bill")
            print("-"*10)
            print("Small Pizza (Rs.50)",n,"nos")
            print("Extra Cheese add-on: Rs.20")
            print("Total Amount:",50*n + 20)
            print("Thank you, Please wait, your order is preparing!")
        else:
            
    case 2:
        print("you've selected medium pizza, please wait your order is preparing")
    case _:
        print("you've selected large pizza, please wait your order is preparing")
