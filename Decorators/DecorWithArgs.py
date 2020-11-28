import functools

def repeat_this(number_of_times_repe):
    def decorator_repeating(function):
        @functools.wraps(function)
        def wrapper_function(*args, **kwargs):
            for _ in range(number_of_times_repe):
                my_result = function(*args, **kwargs)
            return my_result
        return wrapper_function
    return decorator_repeating

@repeat_this(number_of_times_repe=6)
def greet_my_friend(the_name):
    print(f'Hello {the_name}')

greet_my_friend('27-37532')
