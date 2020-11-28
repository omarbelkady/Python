def countingdown(startingnum):
    print('Starting')
    while(startingnum > 0):
        yield startingnum
        startingnum -= 1

generator_obj= countingdown(3)

# How To get the first value of the countdown generator object
val = next(generator_obj)
print(val)
print(next(generator_obj))
print(next(generator_obj))

# The line below will raise an exception
# print(next(generator_obj))
