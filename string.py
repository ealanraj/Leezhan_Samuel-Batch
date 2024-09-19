Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = "hello"
a
'hello'
a[0]
'h'
a[3]
'l'
a[-1]
'o'
a[-2]
'l'
#indexing
a[0]
'h'
#slicing
a[0:3]
'hel'
a[3:]
'lo'
a[-3:]
'llo'
b = "my name is alan"
b[11:]
'alan'
b[-4:]
'alan'
'alan'
'alan'
len(b)
15
for i in range(len(b)):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
for i in range(len(b)):
    print(b[i])

    
m
y
 
n
a
m
e
 
i
s
 
a
l
a
n
chr(65)
'A'
ord("A")
65
chr(97)
'a'
chr(98)
'b'
for i in range(65,91):
    print(chr(i))

    
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
ord("A")
65
ord("")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ord("")
TypeError: ord() expected a character, but string of length 0 found
Z
ord("Z")
90
90-65
25
a
'hello'
a.upper()
'HELLO'
upper()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    upper()
NameError: name 'upper' is not defined. Did you mean: 'super'?
a.upper()
'HELLO'
a.lower()
'hello'
a.lower(d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.lower(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
a.lower("a")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.lower("a")
TypeError: str.lower() takes no arguments (1 given)
a.lower()
'hello'
a = "hello"
len(a)
5
b = " hello"
len(b)
6
b.strip()
'hello'
len(b.strip())
5
b = b.strip()
b
'hello'
c = "   hel lo   "
c.strip()
'hel lo'
c = "  hello   "
c.strip()
'hello'
c.replace("h","k")
'  kello   '
c
'  hello   '
c.split()
['hello']
s = "hi my name is alanraj"
s.strip()
'hi my name is alanraj'
s.strip()
'hi my name is alanraj'
s.split()
['hi', 'my', 'name', 'is', 'alanraj']
s = "hi my name is alanraj"
s = "1,2,3,4,5"
s.split()
['1,2,3,4,5']
len(s.split())
1
s.split()
['1,2,3,4,5']
s.split(",")
['1', '2', '3', '4', '5']
b = ["1-2-3-4-5"]
b.split(",")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b.split(",")
AttributeError: 'list' object has no attribute 'split'
b
['1-2-3-4-5']
b = "1-2-3-4-5"
b.split(",")
['1-2-3-4-5']
b.split("-")
['1', '2', '3', '4', '5']
"a"+"b"
'ab'
a
'hello'
b
'1-2-3-4-5'
a+b
'hello1-2-3-4-5'
a+" "+b
'hello 1-2-3-4-5'
a+","+b
'hello,1-2-3-4-5'
,
SyntaxError: invalid syntax
a="hello"
b="world"
c = a+b
c
'helloworld'
c=a+" "+b
c
'hello world'
"hello"+56
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    "hello"+56
TypeError: can only concatenate str (not "int") to str
c
'hello world'
c.capitalize()
'Hello world'
c = "aaaaabbbbcccdefghi"
c.count("a")
5
c.count("c")
3
c
'aaaaabbbbcccdefghi'
c = a+" "+b
c
'hello world'
c.casefold()
'hello world'
str.casefold()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    str.casefold()
TypeError: unbound method str.casefold() needs an argument
"ABC".casefold()
'abc'
c
'hello world'
c.endswith("d")
True
c.endswith("o")
False
c.startswith("h")
True
"123abc".isalnum()
True
"123ab*c".isalnum()
False
"123".isalnum
<built-in method isalnum of str object at 0x00000176BE3EF510>
(
"123".isalnum()
True
"ajkguaw".isalpha()
True
"123".isalpha()
False
"abc".isascii()
True
"1234".isdigit()
True
"fghjk1235".isdigit()
False
"hello".islower()
True
"A".islower()
False
"A".isupper()
True
"a".isupper()
False
l = ["a","b","c"]
"".join(l)
'abc'
"-".join(l)
'a-b-c'
",".join(l)
'a,b,c'
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
John#Peter#Vicky
"&".join(x)
'J&o&h&n&#&P&e&t&e&r&#&V&i&c&k&y'
x
'John#Peter#Vicky'
l
['a', 'b', 'c']
"&".join(myTuple)
'John&Peter&Vicky'
" & ".join(myTuple)
'John & Peter & Vicky'
a="hello"
" ".join(a)
'h e l l o'
myTuple[0]
'John'
a[0]
'h'
"abcABCcde"
'abcABCcde'
"abcABCcde".swapcase()
'ABCabcCDE'
"my name is alan raj"
'my name is alan raj'
"my name is alan raj".title()
'My Name Is Alan Raj'
'my father\'s name is edward'
"my father's name is edward"
"abc a"
'abc a'
a
'hello'
"abc \a\"
SyntaxError: unterminated string literal (detected at line 1)
"abc "\a"
SyntaxError: unexpected character after line continuation character
"value of a is a"
'value of a is a'
"value of a is \"a"
'value of a is "a'
"value of a is \"a\" "
'value of a is "a" '
'a',a
('a', 'hello')
f"value of a is {a}"
'value of a is hello'
f"the value of a is {a}, and the value of s is {s}"
'the value of a is hello, and the value of s is 1,2,3,4,5'
>>> print("the value of a is ")
the value of a is 
{
>>> print("the value of a is {a}")
the value of a is {a}
>>> print(f"the value of a is {a}")
the value of a is hello
>>> "2 x 5 = {2*5}"
'2 x 5 = {2*5}'
>>> f"2 x 5 = {2*5}"
'2 x 5 = 10'
>>> "the value of a is {}, and the value of s is {}".format(a,s)
'the value of a is hello, and the value of s is 1,2,3,4,5'
>>> "the value of a is {1}, and the value of s is {0}".format(a,s)
'the value of a is 1,2,3,4,5, and the value of s is hello'
>>> "2 x 5 = {}".format(2*5)
'2 x 5 = 10'
>>> "2 x 5 = {}{}".format(2*5)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    "2 x 5 = {}{}".format(2*5)
IndexError: Replacement index 1 out of range for positional args tuple
>>> "2 x 5 = {}{}".format(2*5,100)
'2 x 5 = 10100'
