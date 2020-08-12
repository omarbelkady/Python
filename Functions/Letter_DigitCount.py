j=input()
o = {"THE_#_OF_DIGITS":0,"THE_#_OF_LETTERS":0}
for elem in j:
    if elem.isdigit():
        o["THE_#_OF_DIGITS"]+=1
    elif elem.isalpha():
        o["THE_#_OF_LETTERS"]+=1
    else:
        pass
print("NUM_LET: ",o["THE_#_OF_LETTERS"])
print("NUM_DIG: ",o["THE_#_OF_DIGITS"])
