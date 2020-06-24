#erroredMultsOfThree=genAList(3)
#print(erroredMultsOfThree)

#the above lines of code would error because python is line by line execution.
#This means that if we try to use a variable that we declared below it will error
#In order to use a variable it must be declared above NOT BELOW.
#REMEMBER max in genAList is A PARAMETER. It is the within the function signature
#15 is an argument. It is within your function call

def goPresentYourself():
	print("Hi my name is Omar I love STEM and hate reading")
goPresentYourself()

def genAList(max):
	n=list(range(max))
	for o in n:
		n[o]= o*4
	return n

#This is a multiples of 4 list with 15 elements
multsOfFour=genAList(15)
print(multsOfFour)
print("Above are multiples of 4, as you can C because Alan LOVES C!")
