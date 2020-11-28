def fibonacci(stopping_num):
    # 0 1 1 2 3 5 8 13 21 34
    a, b= 0, 1
    while a < stopping_num:
        yield a
        #update the current value
        a,b = b, a+b
myfib = fibonacci(30)
for iterat in myfib:
    print(iterat)
