## Lists & Dictionaries

### List
- Can store different data types in a list
- Ordered
- Allows duplicates
- Mutable

### How to declare a list

```python
listName=[2,5,3,5,3,5]
listName2=[2, "Nelan", "Olivia", "Mariana", "Angela","Nelan", "Alan5683706342", "0forSpace"]
print(listName2)
```

#### List Methods

|                |Start               |       Method    |Output                         |
|----------------|-----------------|------------|---------------|
|add|▢▢            |.append(▢)            |▢▢▢            |
|clear          |  ▢▢☆         |.clear()            |[]   |
|copy          |  ▢▢▢         |.copy            |▢▢▢   |  
|count          |  ▢▢☆         |.count(▢)            |2   |  
|increase size          |  ▢▢☆         |.extend(js)        where js=[△,△]    | ["▢","▢","☆","△","△"]  |  
|index          |  △▢☆         |.index(△)            |  0 |   
|insert          |  ▢▢☆         |.insert(1,◯)            |[▢,◯,▢,☆]   |
|pop i.e. removes          |  △▢☆         |.pop(1)            |[△,☆ ]   |
|remove          |  ▢☆△         |.remove(△)            |[▢, ☆]   |
|reverse          |  △▢☆         |.reverse()            |[☆ , ▢,  △]   |
|size(i.e. says how big your list/array is)          |  △▢☆         |print(len("△","▢","☆"))       |3   |
|sort          |  [ "z", "e", "l" ]         |.sort()      |[ "e", "l", "z" ]   |

### Slice my original list and place the new list in the old list's memory location aka override var

```python
myNewList=myNewList[0:6]
myNewList.append("ALAN <3 C!!!!")
```

## Tuples

- A tuple is a collection which is:
- Ordered
- Immutable
- In Python tuples are written with parenthesis
- Duplicates allowed

```python
omarTuple=(5,2,3,5,41,4)
print(omarTuple)
print("The number location of 'For Angela: ' is: %d" %omarTuple.index("For Angela: "))
```

## Dictionaries

- A dictionary is a collection which is:
     - Ordered
     - Mutable
     - No Duplicates

### Declaration of a Dictionary

```python
goodMajors={"Alan":"CS", "Waleed":"CS", "Scott": "CS", "Nouhaila":"CSE", "Younes":"CS", "Zakaria":"PE"}
print(goodMajors)
```

### Check if a key exists in a given dictionary by invoking in method:

```python
print("Alan" in goodMajors)
```

#### Delete a key and return to us the associated value

```python
print(goodMajors.pop("Zakaria"))
```

### Print the keys of a dictionary

```python
print(goodMajors.keys())
```

### Sort a dictionary by key

```python
goodMajors={"Alan":"CS", "Waleed":"CS", "Scott": "CS", "Nouhaila":"CSE", "Younes":"CS", "Zakaria":"PE"}
sortedNames=sorted(goodMajors.items(),key=lambda v:v[0])

for x in sortedNames:
    print(x[0],x[1])
```


### Update a value within a dictionary

```python
goodMajors["Alan"]= "2526 56837 7652626"
```
