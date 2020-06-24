# How to declare a list
listName=[2,5,3,5,3,5]

#We can do this in Python unlike other programming languages
listName2=[2, "Nelan", "Olivia", "Mariana", "Angela","Nelan", "Alan5683706342", "0forSpace"]
print(listName2)

print("There are %d list member(s) of Nelan's in this list" %listName2.count("Nelan"))

#To obtain an index of an element with in the list/array listName.index("elementName")

#to add an item to the list append
listName3=["Biology", "Chemistry", "Physics", "ChemE", "EE", "CE", "PE", "ME", "SE", "SyE", "CS", "AsE"]
listName3.append("AnE")

#.append adds to the end of the list and takes only 1 argument

listName3.remove("AnE")

#would Error if I did listName3.remove("ane") because case sensitive

#Reverse the list listName3
listName3.reverse()
print(listName3)


#Create a copy of the list ListName
myNewList=listName3.copy()
myNewList.reverse()

#Slice my original list and place the new list in the old list's memory location aka override var
myNewList=myNewList[0:6]
myNewList.append("ALAN <3 C!!!!")

#To sort a list invoke the sort method .sort()
myNewList.sort()
print(myNewList)

#WE cannot call .sort on a mixed typed array




#<--------------------------TUPLES YOU MONGUE---------------->
"""
MULTI LINE COMMENT FYI
A tuple is a collection which is ordered and unchangeable(no modification, no adding, no removing).
In Python tuples are written with parenthesis unlike lists which are in square
braces [] aka array access in other PL. REMEMBER
once we create a tuple we cannot change it aka immutable. A tuple is a 4 permisson
that means read only. We cannot add/remove. If we try to add/remove we will get a Type Error raised
"""
omarTuple=(5,2,3,5,41,4, "For Angela: ", "6342 56837!!!!!!!!!!!!!!!!!!!!!")
print(omarTuple)
print("The number location of 'For Angela: ' is: %d" %omarTuple.index("For Angela: "))

#<--------------DICTIONARY---------------->
goodMajors={"Alan":"CS", "Waleed":"CS", "Scott": "CS", "Nouhaila":"CSE", "Younes":"CS", "Zakaria":"PE"}
print(goodMajors)

#To print keys only
print(goodMajors.keys())


# Check if a key exists in a given dictionary by invoking in method:
print("Alan" in goodMajors)

#Sort the dictionary for me by key order
#for nameOfKey, nameOfValue in sorted(nameOfDict.items()):
#    print nameOfKey, nameOfValue

#sort the dictionary by key if two keys are the same sort the value
for key,value in sorted(goodMajors.items()):
    print(key,value)
    
#delete an item and do not return the list to me
del goodMajors["Younes"]

#OR YOU CAN USE POP POP POP to delete a key and return to us the associated value
print(goodMajors.pop("Zakaria"))


#print(goodMajors)


#HOW TO MODIFY A value
goodMajors["Alan"]= "2526 56837 6342"
