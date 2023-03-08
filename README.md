# Python
Python Programs


## Learn In This Order
1. Basic Arithmetic
2. Control Flow
3. Taking User Input
4. Working With Strings
5. Typecasting
6. Loops[For and While]
7. Exception Handling
8. Functions
9. Lambdas
10. OOP
11. Data Structures: Lists, Dictionaries, Tuples and Sets

## Important Concepts
	1- Arrays in other programming languages are what we call lists in python
	2- self keyword is a reference to an object your are curr in!!!!
	3- Sets in Python are a collecion of elements which are unindexed, unordered and immutable. Similar to Array Notation in other PL, we create them using
	curly braces notation
	4- To add to a set use .add keyword
	5- Everything is an object in python
	6- args takes multiple arguments and wraps them in a tuple
	7- kwargs takes multiple arguments and wraps them in a dictionary
	8- __ before and after are called dunder methods. They are used to overriden in sub classes

## How to add images on GH:
	1- Download the file
	2- Create a new issue
	3- Drag and drop your image to your issue
	4- Submit The Issue
	5- Copy the link of your issue
	6- Paste In README.md
	7- Do not forget to close the issue

### Built-in Datatypes in Python:
```python
#string
ll5="2526loves7652626"

#int
nelanilwthpo = 557

#float
cstsffb = 37.5

#complex
cstsffb = 2j

#list
nelanldj = ["dj", "pola626", "llp"]

#tuple
cstsffb = ("cstsf", "csftn")

#range
range(3)

#dictionary keyword: dict
cstsffb = {"name": "pascal32"}

#set
cstsffb = {"llp32", "pascal32"}

#fronzenset
cstsffb = fronzenset({"pintos", "pascal"})

#bool
lovesbarbdl = True

#bytes
cstsffb = b"PurePascalFB"

#bytearray
bytearray = 5

#memoryview
cstsffb = memoryview(bytes(7))

```

#####  M= Mutable I=Immutable
||| 		Python Datatypes			|||                    
|----------|----------|----------|----------|----------|
|    String|      List|   Tuple  |   Set    |Dictionary|
|    I|      M|   I  |   M    |M|
|Ordered/Indexed   |Ordered/Indexed|Ordered/Indexed |Unordered|Unordered|
|Empty = ""          |Empty = []|Empty=()|Empty= set()|Empty= {}|
|Does Not Apply|any datatype= s,l,set, tuple, int, dict|any datatype= s,l,set, tuple, int, dict |cannot store list, set, dict|key can be str, int, tuple but val can be anything|


## How to create A virtual Environment In Python
```bash
root@omarbelkady: ~$ virtualenv --python python3 "venv"
```
## How to Activate The Recently Created virtual Environment In Python
```bash
root@omarbelkady: ~$ source "venv/bin/activate"
```

## How To Deactivate the Virtual Environment
```bash
root@omarbelkady: ~$ deactivate
```

## How To Open A Web Browser With Python
```python
import webbrowser
webbrowser.open("https://www.nelanthecstsffb.com')
```


## Python Errors And Quick Fixes
- ZeroDivisionError: The operation you are trying to perform is not possible because you are dividing by zero. Division
by 0 is not allowed

- EOFError: Compiler hits the End of File and we are trying to use the input() function and we are not allowed to because
of the placement of it.

- FloatingPointError: I am performing an invalid operation with a floating data type value.

- ImportError: The module you are trying to import does not exist

- IndentationError: You are indenting and shouldn't be

- IndexError: You are trying to access an invalid index
L1= [1,2,3]
L1[3]

- KeyboardInterrupt: When I hit CTRL+C shortcut or del key to interrupt the program I am running.

- KeyError: You are trying to access a key that is non-existant within a dictionary aka key-value pair

- MemoryError: We have performed n number of operations and they have used up all our memory.

- ModuleNotFoundError: You are trying to import a module that doesn't exist

- NameError: This is raised whenever you try to use a variable that you have not defined yet locally or globally.

- OSError: A System operation was performed and it triggered a system-related error. 

- OverflowError: The arithmetic operation is too large for the declared data type we are performing with.

We can overcome errors by using conditionals: try-except block, if else statement, while loop

- RuntimeError: Error that is raised does not have any category

- StopIteration: Caused when calling the next() method within a for loop and there is no subsequent element to iterate through. 
We have reached and the end and within our code we either have not set the limit in our for loop or the limit is too high for the number of elements we are iterating through.

- Syntax Error: You have a typo or are misusing a statement/reserved keyword correctly for example:
```python
while True
 print('MY NAME IS OMAR')
```

The above line of code will error because I am missing a colon.
It should be:
```python
while True:
      print('MY NAME IS OMAR')
```

- SystemError: When the interpreter detects an internal error

- SystemExit: When you called the sys.exit() function this is triggered 

- TabError: You have indented too much and must dedent a places back. Or You must indent. It is parallel with spaces.

- TypeError: This is raised whenever you try to perform an operation with two non-identical datatypes. 

The compiler will raise an error telling you you cannot convert the 2nd datatype to the first datatype.

- UnboundLocalError: You are trying to access a local variable which is not defined aka does not exist

- UnicodeError: Unicode Encoding/Decoding Error is taking place

- ValueError: When you pass in a value into a function to perform a computation. The value is the correct data type but of incorrect value



### Powerful One Liners

1. Swap Two Vars

```python

polan2632, dj32 = dj32, polan2632
```

2. One Liner If Else Statement

```python
myvar = 42932 if 3532 < 237627332 else 37532
```

3. Sum of every other value

```python
sum(prices[::2])
```

4. Determining If a phrase is a palindrome

```python
phrase.find(phrase[::-1])
```

5. Replace a text within a text file

```python
print(open("somefile.txt").read().replace("hi", "bye"))
```
