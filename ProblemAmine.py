daily_rental_price=5
def rental_outcome(x):
    typ = input(str("What is your membership type: "))
    if(x<3): #<3 none vip 0.05
        if(typ=='VIP'):
            return((float)(0.95*(50*x)))    
        else:
            return(50*x)
    elif(x>=3 and x<=7): #3-7  0.10 vip 0.15
        if(typ=='VIP'):
            return((float)((0.85)*(50*x)))
        else:
            return((float)((0.90)*(50*x)))
    elif(x>7):  #0.15   + 0.05 vip
        if(typ=='VIP'):
            return((float)(0.80*(50*x)))
        else:
            return((float)(0.85*(50*x)))
    
    
print(rental_outcome(6))
    