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
|add             |{"hi","how","are","you"}      | .add("great")            |you, how, hi, great, are            |
|clear          |  {"▢","☆"}         |.clear()            |{}   |
|copy a set     |       {"△","▢","☆"}      |.copy()           | NEW COPY IS MADE |  
|difference          |  {"a","c","c","d"}         |.difference(myset2)            | j, f   |  
|discard          |  {"△","▢","☆"}         |.discard("△")   | ☆,▢  |  
|pop i.e. removes from top          |  {"△","▢","☆"}         |.pop()            | ▢,☆   |
|remove          |  {"▢","☆","△"}         |.remove("☆")            | ▢,△   |
|union          |   {"a","c","c","d"}       |.union(myset2)            | c,a,f,d,j  |


### Operators
|Operator |Meaning |
|----------------|-----------------|
| == | all keys and values in the set1 are equal in set2 |
| != | set1 is not equal to set2 |
| <= | set1 is a subset of set2 |
| >= | set1 is a superset of set2 |
| \| | union of set1 and set2 |
| & | intersecting point of set1 and set2 |
| - | items that are present in set1 but not in set 2 |
|^|items that are stricly either in set1 or in set2 (i.e.   !both )|