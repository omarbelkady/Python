class EnjoyLLP():
    pass

class IsACLover():
	#This is my constructor
	def __init__(self, name,title):
		self.name = name
		self.title = title


class FavActivit():
    def __init__(self, activity):
        self.activity=activity

#Object 1
pintosLover=FavActivit("Nelan Loves Pintos WayTooMuch")
print(pintosLover.activity)

#object 2
alan = EnjoyLLP()


#object 3
nelan = IsACLover("Nelan", "CDeveloper")
if(nelan.title=="CDeveloper"):
    print("Nelan The Best Person To help you in C And Assembly")


