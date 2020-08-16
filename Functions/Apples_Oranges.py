'''return apples if given a string
return oranges if given an integer
return bananas if given anything else
'''
def fruit_type(fruit):
    if(type(fruit) == int):
        return "Oranges"
    elif(type(fruit) == str):
        return "Apples"
    return "Bananas"

print(fruit_type(4))
print(fruit_type("Nelan"))
print(fruit_type(1493.123))
