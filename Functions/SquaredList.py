def listOfSquares():
    myList=list()
    for i in range(4,25):
        myList.append(i**2)#square the numbers 4 to 24 and add them to the list
    print(myList[7:])#print the eighth element to the end

#Call The Function
listOfSquares()
