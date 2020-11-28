import functools
def start_and_end_decor(function):
    #preserve the info of my used function
    @functools.wraps(function)
    def wrapper_func(*args, **kwargs):
        # Do Sth before the function call
        # extend the behavior
        print("Starting!!!")

        # Within my wrapper function I execute the function
        my_output= function(*args, **kwargs)
        
        # Do Sth After the function call
        # More extending behavior
        print("Ending !!!!")
        return my_output
    return wrapper_func


@start_and_end_decor
def incrementby6(z):
    return z+6

#Applying the function to the  decorator below and supplying an argument of printSth
#incrementby6=start_and_end_decor(print_Sth)

# This will raise the exception wrapper function takes 0 positional arguments but 1 was given
my_output = incrementby6(6)

'''
To fix this error I add the parameters:
    - *args
    - **kwargs
which will allow me to have as many arguments and keyword arguments as I wish
'''
# This wil output none to do that I must store the function output in a variable
print(my_output)

# How To print the function name of the decorator meaning the function who called it in the function
print(incrementby6.__name__)
