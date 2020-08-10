def myFun(*argv):  
    ret = ""
    for arg in argv:  
        ret+= arg+ " "
    return ret
    
#REMEMBER THIS IS A TUPLE
computer = ("Asus", "MSI", "Eluktronics", "Gigabyte", "Unbox")
print(myFun('Hello', 'Welcome', 'to', 'My Repo',"Please", "Remind", "Alan That He", "Likes:", "C++","Java", "Python"))


'''THIS WOULD ERROR BECAUSE () INDICATES IT IS A TUPLE '''
# computer[5]="Unbox"
