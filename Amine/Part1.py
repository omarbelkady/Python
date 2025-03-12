for i in range(1,11, 1):
                #range([start,stop),step)
    print(i)

def factorial(i):
    if(i<1):
        return "Factorial cannot be negative"
    if(i==1 or i==0):
        return 1
    else:
        return i*factorial(i-1)
print(factorial(6))


def squarenumb(nums):
    squares = []
    for num in nums :
        squares.append(num*num)
    return squares


print(squarenumb([5,6,8,8,9]))