## OOP in Python

```python
class IsACLover():
	#This is my constructor
	def __init__(self, name,title):
		self.name = name
		self.title = title
	
	#This is my deconstructor
	def __del__(self):
		print("The insect instance of " + self.__name__+ " was just destroyed")

nelan = IsACLover("Nelan", "CDeveloper")
if(nelan.title=="CDeveloper"):
	print("Nelan The Best Person To help you in C And Assembly")
```

### How To Create Class With Attributes

```python
class SoccerPlayer:
	fName="Lionel"
	lName=" Messi"
	age=34

# How To Delete the attribute age
delattr(SoccerPlayer, "age")

richard = {
	'major': 'CS',
	'gender': 'Male',
	'age': 29

}

# Right Way to Get An Attribute
print(richard.get(age))
```