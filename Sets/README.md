## Sets

- Unordered Collection
- Mutable 
- Iterable
- No Duplicate Vals

### Declaring A Set

```python
myset={"Bye", "Hi", "In A While"}
myset1 = {"a","c","c","d"}

myset2={"f","c", "j"}
```



|                |Start               |       Method    |Output                         |
|----------------|-----------------|------------|---------------|
|add|{}            | {} | .add(▢)            |{▢}            |
|clear          |  ▢☆         |.clear()            |{}   |
|copy a set     |       △▢☆       |.copy()           |▢▢▢   |  
|difference          |  "a","c","c","d"         |.difference(myset2)            | { "j", "f"}   |  
|discard          |  △▢☆         |.discard("△")   | {"▢", "☆"}  |  
|pop i.e. removes from top          |  △▢☆         |.pop()            | {"▢","☆" }   |
|remove          |  ▢☆△         |.remove(☆)            |[▢,△ ]   |
|union          |          |.union(myset2)            |{"c", "a", "f", "d", "j"}   |

