def start_and_end_decor(function):
    def wrapper_func():
        # extend the behavior
        print("Starting!!!")

        # Within my wrapper function I execute the function
        function()

        # More extending behavior
        print("Ending !!!!")
    return wrapper_func

# decorator syntax 
#@mydecorator
#def doSth():
#    pass

# the line below is the same as line 24
@start_and_end_decor
def print_Sth():
    print("Nelan 47 2 557 263 27-375 32!")

#Applying the function to the  decorator below and supplying an argument of printSth
#print_Sth=start_and_end_decor(print_Sth)
print_Sth()
