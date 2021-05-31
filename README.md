# Python
Python Programs


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
