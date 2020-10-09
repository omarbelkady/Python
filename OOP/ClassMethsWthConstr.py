class IsABookLover():
    def __init__(self, name, pages):
        self.name=name
        self.pages=pages

    #anytime you put a class method you must supply the self keyword as a parameter
    def is_long(self):
        if(self.pages >7):
            print("You Will die and Angela will be your cause")
            return True
        return False
        


Nelan = IsABookLover("NelanNotABookLover But A CLover", 2)
Angela = IsABookLover("Angela", 599)
print(Angela.name + " is going to kill you for sure!")
print(Nelan.name + " will not kill you ")
print(Nelan.is_long())
print(Angela.is_long())
