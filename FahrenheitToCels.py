temperature=int(input("Please provide a temperature: "))
CF= input("Is this in Celsius or Fahrenheit, mention with C or F")
if(CF== "C" or CF== "c"):
    result=((temperature+32)*(9/5))
    print(str(result))
elif(CF== "F" or CF== "f"):
    result=((temperature-32)*(5/9))
    print(str(result))

