### Lists And Functions
```python
# How To Reverse A List with Slicing #1
favlangs=["pascal", "cobol", "machine code"]
#### Printing the reverse of the list
print(favlangs[::-1])
```

```python
# How To Reverse A List with Slicing #2
favlangs=["pascal", "cobol", "machine code"]
#### Printing the reverse of the list way2
favlangs.reverse()
print(favlangs)
```


```python
# How To Find An Item within A List
favlangs=["pascal", "cobol", "machine code"]
if 'assembly' in favlangs:
	print(favlangs.index("pascal"))
elif 'cobol' in favlangs:
    print(favlangs.index("cobol"))
else:
    print("definittttely a llpfb")
```
