mystring="Hello Omar Belkady I am 234adkk whatever"
print(mystring[6:15])
value = mystring.rindex("Belkady")
def myfunction(some_string,target):
    position = some_string.find(target)
    if(position != -1):
        return position
    else:
        return False
print(myfunction(mystring, "Drari"))
print(myfunction(mystring, "whatever"))
print(value)


sentence= "to be or not to be that is the question that should be asked"
print(sentence.count("that", 13, -1))