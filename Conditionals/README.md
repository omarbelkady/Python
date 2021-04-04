### Conditionals in Python
```python
num = 2222
if(1<num<10):
    print("This is a one digit number")
elif(11<num<100):
    print("This is a two digit number")
elif(101<num<999):
    print("This is a three digit number")
elif(num >= 1000):
    print("4 digit number")
```


### Menu using a conditional within a function
```python
def my_menu():
    print("Welcome to the Professor Fan Club!! Make a choice\
    \n 1.7olan2oFB\
    \n 2. 3JFanb69\
    \n 3. 429FB\
    \n 4. 227243 3655FB\
    \n 5. Coding Low Level")
    option= int(input("What type of fan are you"))
    if option == 1:
        print("968\'re a 76lan2o FB\n\n")
    elif option == 2:
        print("DJ Fanboy\n\n")
    elif option == 3:
        print("Computer Arch is the best thing ever\n")
    elif option == 4:
        print("Bar243 56837 933333333333333333333333324\n")
    elif option == 5:
        print("LLP is the best thing ever\n")
    elif ValueError:
        print("That was a wrong choice")
        my_menu()
    else:
        print("Done")
my_menu()
```
