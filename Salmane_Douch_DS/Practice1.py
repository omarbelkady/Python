def calc_average():
    count=int(input("Please enter the number of values you would like to take the average: "))
    total=0
    for x in range(count):
        number=float(input("Enter a number: "))
        total+=number
    if(count==0):
        return("No numbers provided")
    else:
        return total/count
result=calc_average()
print("The result is: "+str(result))
