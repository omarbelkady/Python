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
