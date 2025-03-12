import math
#function
def factorial(num):
    if(num == 1):
        return 1
    else:
        x = num * (num-1)
        return x
print(factorial(4))
def factorial2(num2):
    for i in range(1, num2):
        num2 = num2*i
    return num2

mylist1=[1,2,3]
def calc_average(mylist1):
    for i in mylist1:
        sum56=sum(mylist1)
        average = sum56/len(mylist1)
        return average
print(calc_average(mylist1))

def fahrenheit(celsius):
    f= (9/5*celsius)+32
    return f

def add_two_number(num1=2, num2=3):
    return num1+num2

print(add_two_number(3))
print(add_two_number(2,7))
print(add_two_number())

#glo
num33=8
#local scope
def local_global_scope():
    global num7
    num7 = 8
    num1=3
    return num1

local_global_scope()

def print_stars():  #down
    num = int(input("Enter a number"))
    for i in range(1, num+1):
        for j in range(i):
            print("*",end=' ')
        print()
    return ""

def print_stars_up():  #down
    num = int(input("Enter a number"))
    for i in range(num,0,-1):
        for j in range(i):
            print("*",end=' ')
        print()
    return ""
print(print_stars())
print(print_stars_up())