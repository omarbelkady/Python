import numpy as np
def swtch_func(eulav, o):
    return{
        '1':lambda o:o**2,
        '2':lambda o:o**0.5,
        '3':lambda o:np.log(o)
    }.get(eulav)(o)
your_choicee=input("Please select your option: ")
print("You chose option",your_choicee,"which outputs to ",swtch_func(your_choicee, 81))
