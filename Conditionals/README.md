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

### Menu Type 3:
```python
def my_menu():
    print("Welcome to the Conversion Calculator which option would you like\
    \n a. Miles to Kilometers\
    \n b. Gallons To Liters\
    \n c. Pounds to Kilograms\
    \n d. Inches To Cm\
    \n e. Fahrenheight To Celsius")
    option= str(input("Which type of conversion are you wishing to perform:     "))
    if option == 'a' or option == 'A':
        print("\n\nYou are converting Miles to Km")
        n = float(input("What is amount of miles you wish to convert to km?: "))
        s = milesToKm(n)
        print("%.2f"%s)
    elif option == 'b' or option == 'B':
        print("\n\nYou are converting Gallons to Liters")
        g = float(input("\nWhat is amount of gallons you wish to convert to liters?:  "))
        b=gallonsToLiters(g)
        print("%.2f"%b)
    elif option == 'c' or option == 'C':
        print("\n\nYou are converting Pounds to Kg")
        l = float(input("\nWhat is amount of lb you wish to convert to kg?:  "))
        c=lbsToKg(l)
        print("%.2f"%c)
    elif option == 'D' or option == 'D':
        print("\n\nYou are converting Inches to Cm")
        d = float(input("\nWhat is amount of Inches you wish to convert to Cm?:  "))
        e = inchesToCm(d)
        print("%.2f"%e)
    elif option == 'e' or option == 'E':
        print("\n\nYou are converting Fahrenheight To Celsius")
        cels = int(input("\nWhat is the temperature in Fahrenheight you wish to convert to Celsius?:  "))
        h = fahrenToCels(cels)
        print("%.2f"%h)
    elif ValueError:
        print("That was a wrong choice")
        my_menu()
    else:
        print("Done")

def milesToKm(miles: int) -> float:
    return miles*1.60934
def gallonsToLiters(gallons: float) -> float:
    return gallons*3.78541
def lbsToKg(pounds: float) -> float:
    return pounds*0.453592
def inchesToCm(inches: float) -> float:
    return inches*2.54
def fahrenToCels(fahren: float) -> float:
    return((fahren-32)/1.8)
my_menu()
```
