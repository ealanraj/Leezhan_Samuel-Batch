
# try:
#     file = open("fruits.txt")
#     content = file.read()
# except FileNotFoundError:
#     print("File is not found!")
# else:
#     print("The file is opened successfully")
#     print(content)
# finally:
#     file.seek(0)

#read

# print(file.read(5))

# file.close()


#readline

f = open("fruits.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

#reading using loop

for i in f:
    print(i)
    
#close function

f.close()

#writing to an existing file
'''
1. 'a' - append
2. 'w' - write
'''

f = open("fruits.txt",'a')
f.write("\nstrawberry")
f.close()

f = open("fruits.txt")
print(f.read())

#write

f = open("fruits.txt","w")
f.write("Oops!, I deleted the entire content mistakenly!!")
f.close()

f = open("fruits.txt")
print(f.read())
f.close()

# try:
#     f = open("fruit.txt","x")
# except Exception as e:
#     print(e)
# else:
#     print("the file created successfully")
# finally:
#     f.close()
    
def readFile(path):
    try:
        f = open(path)
        content = f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        f.close()

        
readFile("fruits.txt")


def create(name):
    try:
        f = open(name,"x")
    except Exception as e:
        print(e)
        
create("fruit.txt")
    
def deleteFile(path):
    try:
        f = open(path)
        f.close()
    except Exception as e:
        print(e)
    else:
        import os
        os.remove(path)
        print("the file deleted successfully!!")
        


deleteFile("fruit.txt")


with open("fruits.txt") as f:
    content = f.read()
    print(content)   

