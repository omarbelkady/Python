def my_generator():
    yield 55732
    yield 2737532
    yield 2626532
    yield 72722532

assembfb = my_generator()
# how to loop a generator
'''
for pfb in assembfb:
    print(pfb)
'''

# how to return the next item in the generator and pauses
val = next(assembfb)
print(val)

# How to print 2nd item in the generator and also pause
val = next(assembfb)
print(val)

# How to print 3rd item in the generator and also pause
val = next(assembfb)
print(val)

# How to print 4th item in the generator and also pause
val = next(assembfb)
print(val)


# val = next(assembfb)
# print(val)
'''
line 31 and 32  will error and raise a StopIteration Exception because 
there are no more elements to iterate over

A Generator will always raise a StopIteration Exception if it doesn't
reache another yield statement
'''

# Using the generator to calculate the sum of the elements within it
print(sorted(assembfb))
