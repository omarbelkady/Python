def fibonacci(x):
    if x == 0: 
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

j= int(input("Please enter the nth number you wish to calculate the Fibonacci of: "))
some_vals = [str(fibonacci(x)) for x in range(1,j+1)]
print(",".join(some_vals))
