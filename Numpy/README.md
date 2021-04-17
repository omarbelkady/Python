## Numpy
- Python library used heavily in ML and DS to perform mathematical and logical operations on arrays


### How To Install
```bash
sudo apt-get install python-numpy 
```

### Data Types
- Boolean -> bool
- Integer(default) -> int_...same as C's long data type
- Integer(C family) -> intc ... same as C's int
- intp->: Integer used for indexing (same as C ssize_t; normally either int32 or int64)
- int8-> integer
- int16 -> integer with a bigger range than int8
- int32 -> integer with a bigger range than int16
- int64 -> integer with a bigger range than int32
- uint8 -> unsigned int
- uint16 -> unsigned int
- uint32 -> unsigned int
- uint64 -> unsigned int
- float_ -> floating data type
- float16 -> floating data type has a bigger range and is more precise than a float
- float32 -> floating data type has a bigger range and is more precise than a float16
- float64 -> floating data type has a bigger range and is more precise than a float32
- complex_ -> complex data type 
- complex64 -> complex data type with more precision than an ordinary complex
- complex128 -> complex data type with more prevision than a complex64

### Character code for data type in Numpy

1. 'b': boolean
2. 'i': signed integer
3. 'u': unsigned integer
4. 'f': floating point
5. 'c': complex floating point
6. 'm': time delta
7. 'M': datetime
8. 'O': Python Objects
9. 'S', 'a': String
10. 'U': Unicode

11. 'V': raw data


### How To resize an ndimensional array
```python
import numpy as np 

a = np.array([[2,4,9],[3,5,7]]) #this is a 2x3 array
a.shape = (3,2) # it will now become a 3x2 aka transpose the array

print a 
#way number 2
m = np.arange(24) #an array of 24 elements aka 0 through 23 
a.ndim  

# now reshape its 2 separate arrays, 4 rows, 3 columns
b = a.reshape(2,4,3) 
print b 
```

### Array Indexing
```python
import numpy as np 
a = np.arange(10)  # fill array with 10 elements
s = slice(2,7,2)  # start at 2 stop 7 step 2 aka 2,4,6
print a[s]
```

### How To Iterate Through An Array Using a range-style built-in function of numpy
```python
import numpy as np
ftn = np.arange(0,60,5) # start at 0 stop at 60 step 5 numbers
ftn = ftn.reshape(3,4) # turn the array into 2d

print 'Original array is:'
print ftn
print '\n'

# Transpose of the array
print 'Transpose of Array:' 
b = ftn.T 
print b 
print '\n'  

print 'Modified array is:'
for x in np.nditer(b):
   print x
```