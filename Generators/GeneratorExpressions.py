import sys
# Generator Expressions are written the same way as List Comprehensions USING PARENTHESIS INSTEAD OF SQUARE BRACKETS
mygen = (cstsffb for cstsffb in range(10) if cstsffb % 2 == 0)
for pascfb in mygen:
    print(pascfb)

# Casting my generator object mygen to a list
print(list(mygen))


print("Here is why we use a generator when dealing with a million numbers: \n\n")
mygenerat = (i for i in range(1000000) if i%2 == 0)
print(sys.getsizeof(mygenerat))

print("\n\nHere is how much memory you will when using a list that will house a million numbers..Notice IT IS MUCH MUCH MORE!")
alist = [i for i in range(1000000) if i%2 ==0]
print(sys.getsizeof(alist))
