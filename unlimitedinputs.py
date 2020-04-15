def add_numbers(*args):#the *args keyword lets you input multiple arguments
    total=0
    for a in args:
        total+=a
    print(total)
add_numbers(3)
add_numbers(4,5,6,9)
add_numbers(19,24,94891)
