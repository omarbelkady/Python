def product_average(*args):
    if(len(args)==0):
        return
    product = 1
    total = 1
    for number in args:
        product*=number
        total+=number
    average=total/len(args)
    return(f"Product: {product:.2f} and Average: {average:.2f}")

print(product_average(2,3,4))
print(product_average(4,4,1,4,14221,4223))
print(product_average())