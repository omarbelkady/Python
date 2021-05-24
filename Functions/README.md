# Lists And Functions

## How To Reverse A List with Slicing #1
```python
favlangs=["pascal", "cobol", "machine code"]
#### Printing the reverse of the list
print(favlangs[::-1])
```

## How To Reverse A List with Slicing #2
```python
favlangs=["pascal", "cobol", "machine code"]
#### Printing the reverse of the list way2
favlangs.reverse()
print(favlangs)
```


## How To Find An Item within A List
```python
favlangs=["pascal", "cobol", "machine code"]
if 'assembly' in favlangs:
	print(favlangs.index("pascal"))
elif 'cobol' in favlangs:
    print(favlangs.index("cobol"))
else:
    print("definittttely a llpfb")
```

## Learn what operations you can perform on an element
```python
a_string= "Hello There"
print(dir(a_string))
```


## Arrow Functions in Python with input type and output type specification
```python
def isACSTSFFB(name: str) -> bool:
    if(name == "nelan"):
        return True
    else:
        return False
```

### Creating a Function with positional args

```python
def persninfo(name, job):
    print("\nMy name is "+ name + ". ")
    print(" and I am a(n) "+ job +". ")
persninfo("ftnfanb", "429 TA")
    
```


### Creating a Function with default value

```python
def persninfo(name, job="developer"):
    print("\nMy name is "+ name + ". ")
    print(" and I am a(n) "+ job +". ")
persninfo("ftnfanb")
    
```


### Using a keyword argument

```python
def petsAndInfo(name, numOfPets):
    print("My name is "+ name + " and I have "+ numOfPets + " pet(s).")
```
### Making the argument optional 

```python
def petsAndInfo(name, numOfPets=None):
    print("My name is "+ name)
    if(numOfPets):
        print(" and I have " + numOfPets + " pet(s).")
petsAndInfo("Bob", str(5))
petsAndInfo("Tracy")
```

### Returning A Dictionary

```python
def myFullName(fName, lName):
    individ = {"First Name": fName, "Last Name": lName }
    return individ
bookfb = myFullName("Angela", "Cao")
print(bookfb)
```

### Taking A List as an argument

```python
def sayHiToGuests(people): 
    for person in people: 
        message = "Hi, " + person + "!"
        print(message)
peeps = ["Joey", "DJ", "Pascal"]
sayHiToGuests(peeps) 
```

