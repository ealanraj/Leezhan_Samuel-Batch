# function assigned to a variable
def shout(t):
    return  t.upper()

print(shout("helloo!"))  

yell = shout

print(yell("abcdefghijklmnopqrstuvwxyz"))

def whisper(t):
    return t.lower()

# function passed as an argument

def greet(func):
    return func("Good Morning!!, I am created by the function passed by an argument")

print(greet(shout))
print(greet(whisper))

#function can return another function

def create_adder(x):
    def adder(y):
        return x+y
    
    return adder

add_100 = create_adder(100)
add_50 = create_adder(50)

print(add_100(100))
print(add_50(50))

#decorator function:-

# def decorator(func):
#     def wrapper():
#         print("adding something before the function is called!")
#         func()
#         print("adding something after the function is called")
#     return wrapper

# @decorator

# def sayHello():
#     return "Hello by original function!!"

# print(sayHello())


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called")
        return func(*args, **kwargs)
    return wrapper


@decorator

def say_hello(name):
    return f"Hello, {name}!"

# Call the decorated function
print(say_hello("Alan"))
