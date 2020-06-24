#<-----------------VARS ARE CONTROLLED BY SCOPE---------------->
"""
C-LANGUAGE SCOPE RULES

scope level a

    if(bla)
        scope level b
    else if
        scope level c

scope level d

variable declared in scope level a.... available in level: b,c,d
variable declared in scope level b.... available in level: b ONLY
variable declared in scope level c.... available in level: c only

ALL IN ALL THIS KEEPS THINGS ENCAPS WITHIN OUR CODE
"""

#This is a conditional  1 (=) is assignment 2(=) meaning == is comparison
nelan= "Alan took C with 6342"

if nelan == "Alan took C with 6342":
    print("Alan 56837 NEHA!!!!!!!")

faultyAlan= "Literature"
if faultyAlan != "CS":
    print("GET OUT OF HERE!")

major = "CE"
gameLover= True
if major== "CS" and gameLover:
    print("TRUE HERO")
elif major=="CS" or gameLover:
    print("We can still be friends")
else:
    print("You have not met the criteria for me to be your friend")
    
#CHECKING IF AN ITEM IS A MEMBER OF A LIST
majors = ["Finance", "CS", "GameDev", "PE", "SE", "SyE", "ME", "EE", "CE"]
if major in majors:
    print("You are a boss my friend!")
else:
    print("Your major is not in the list!")
    
#Comparing
c=(2,4,9,16,25,36,49,64,81)
d=(3,9,27,81)
elems_in_both_lists = set(c) & set(d)
print("the 2 lists share the following element(s): "+str(elems_in_both_lists))
