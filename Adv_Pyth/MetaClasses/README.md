### Metaclasses
```python
'''
imagine I create a function and created a class within it and the function returned the class Name
this would not be fine in other programming language because it must be the other way around
the function should be within the class. This is okay because in function classes are not classes
they are actually objects
'''
def sayHello():
    class Hi:
        pass
    return Hi
```

### Characteristics of An Object
- interract with it at runtime
- pass it around through params and variables
- store it, save it, modify it and interract with it

### Why is a class an Object in Python
- well that means that there must of been a higher level class that created the object

### What differs a Metaclass from a Class
- A metaclass defines rules for a class
- When I create a class in Python the python interpreter will use the metaclass to create it without you knowing it
- A MetaClass is Superior than A Class

### Proof that everything in Python is an object
```python
class MyClass():
    pass
def myfunction():
    pass
print(type(MyClass())) #outputs class and the 2nd output is actually an object in hexadecimal
print(type(2)) # outputs class int which means the object int
print(type(myfunction)) # outputs class function which means the object myfunction
print(type(MyClass)) 
# outputs class MyClass. MyClass is what is referred to as a metaclass. This Means when I call MyClass I call a type constructor 

MyClass = type('MyClass', (), {})
#              thename    basesmeaninganythingIInheritFrom     attributes

# the statement above is exactly equivalent to where I say class MyClass() pass above

```

```python
#example2
Llpfb = type('Llpfb', (),{"favClass":"CS375"})
cobfb = Lllpfb()
print(cobfb.favClass)
```




### Metaclasses

```python
'''
imagine I create a function and created a class within it
 and the function returned the class Name

this would not be fine in other programming language because it 
must be the other way around

the function should be within the class. 
This is okay because in function classes are not classes

they are actually objects

'''
def sayHello():
	class Hi:
		pass
	return Hi
```

### REMEMBER ALL METACLASSES MUST INHERIT FROM TYPE
```python
class MyClass(type):
    #this is called before init we can change values in init but not in new
    def __new__(self, class_name, bases, attr):
        print(attr)
        return type(class_name, bases, attr)

class LLPFB(metaclass="MyClass")
    favParad=26265
    favOS=746867

#Creating an instance of LLPFB
l = LLPFB()
```

  

### Characteristics of An Object

- interract with it at runtime

- pass it around through params and variables

- store it, save it, modify it and interract with it

  

### Why is a class an Object in Python

- well that means that there must of been a higher level class that created the object

  

### What differs a Metaclass from a Class

- A metaclass defines rules for a class

- When I create a class in Python the python interpreter will use the metaclass to create it without you knowing it

  

### Proof that everything in Python is an object

```python
class MyClass():
	pass

def myfunction():
	pass

print(type(MyClass())) #outputs class and the 2nd output is actually an object in hexadecimal

print(type(2)) # outputs class int which means the object int

print(type(myfunction)) # outputs class function which means the object myfunction

print(type(MyClass))

# outputs class MyClass. MyClass is what is referred to as a metaclass. This Means when I call MyClass I call a type constructor

MyClass = type('MyClass', (), {})
# the statement MyClass is exactly equivalent to MyClass Class Definition
```
