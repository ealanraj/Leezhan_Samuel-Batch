try:
    n = int(input("enter a number : "))
except:
    print("check your entered value!")
else:
    print(f"the square value for the number you've entered is {n*n}")
finally:
    print("All blocks executed successfully!")
    
print("Leezhan Branch")