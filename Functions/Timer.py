from timeit import Timer
#Given a number inputed to range this calculates how much time it takes to perform the computation inputted
my_time=Timer("for j in range(3):1+1")

print(my_time.timeit())
