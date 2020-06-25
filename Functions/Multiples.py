def genAList(max):
	n=list(range(max))
	for o in n:
		n[o]= o*4
	return n

#This is a multiples of 4 list with 15 elements
multsOfFour=genAList(15)
print(multsOfFour)
