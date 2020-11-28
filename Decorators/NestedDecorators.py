import functools
def starting_and_ending_decorator(func):
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        print("Beginning of the decorator: ")
        response = func(*args, **kwargs)
        print("Ending of the Decorator")
        return response
    return wrapper_function


def debug(function):
    @functools.wraps(function)
    def wrapper_function(*args, **kwargs):
        argument_represent = [repr(a) for a in args]
        kwargs_represent = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(argument_represent + kwargs_represent)
        
        #print the information of the function
        print(f"I am calling {function.__name__!r}({signature})")

        #executes the function
        result = function(*args, **kwargs)
        
        # print information about the return value of the function
        print(f"{function.__name__!r} returned {result!r}")
        return result
    return wrapper_function


# I decorate my present_yourself with a second decorator called debug and debug function will be exec first 
# then starting_and_ending decorator

@debug
@starting_and_ending_decorator
def present_yourself(yourname):
    greet_yourself = f'Hello There {yourname}'
    print(greet_yourself)
    return greet_yourself
