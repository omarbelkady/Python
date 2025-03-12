def running_total1():
    total=0
    print("Enter the numbers to add to the total. -1 to stop")
    while(True):
        try:
            number= float(input("Enter the number"))
            if(number==-1):
                print(f"The total sum is: {total}")
                break
            total+=number
        except:
            print("Invalid Input")
running_total1()


def running_total():
    total=0
    while True:
        try:
            x = float(input("Enter the numbers to add and -1 to stop"))
            if(x==-1):
                break
            total+=x
        except ValueError:
            print("Invalid Input")
    print(f"The total is: {total}")
running_total()


