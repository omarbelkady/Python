my_inp = input()
comput= {"UPPER":0,"LOWER":0}

for elem in my_inp:
    if elem.isupper():
        comput["UPPER"]+=1
    elif elem.islower():
        comput["LOWER"]+=1
    else:
        pass

print("UPPER CASE ITEMS#: ",comput["UPPER"])
print("LOWER CASE ITEMS#: ",comput["LOWER"])
