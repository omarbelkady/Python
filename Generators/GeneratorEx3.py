import sys
def firnelem(x):
    numbers_list = []
    starting_num = 0
    while starting_num < x:
        numbers_list.append(starting_num)
        starting_num += 1
    return numbers_list

# print(firnelem(6))

# Print the sum of the n elements
# print(sum(firnelem(7)))

print("\n\nUsing a Generator Instead")

def my_firnelem_usin_a_generator(x):
    starting_num = 0
    while starting_num < x:
        yield starting_num
        starting_num+=1
# Notice I do not need a list aka array to save all the numbers
print(sum(my_firnelem_usin_a_generator(7)))

# Now I will see how much memory I use without a generator
print(str(sys.getsizeof(firnelem(10)))+" is how much memory I use without a generator")

# Now I will see how much memory I use witha generator
print(str(sys.getsizeof(my_firnelem_usin_a_generator(10)))+" is how much memory I use without a generator")
