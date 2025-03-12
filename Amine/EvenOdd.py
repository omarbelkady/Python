pos=0
neg=0
odd=0
even=0
while(True):
    num=int(input("Please enter a number"))
    if(num != 0):
        if(num>0):
            pos+=1
        elif(num<0):
            neg+=1
        if(num%2==0):
            even+=1
        elif(num%2!=0):
            odd+=1
    else:
        break
print(f"Positive Number: {pos}, Negative Number: {neg}, Odd Number: {odd}, Even Number: {even}")

