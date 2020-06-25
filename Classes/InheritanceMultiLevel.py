class Animal(object):
    name= " "
    
    def eat(self):
        #%s is mapped to whatever argument we pass in for the object
        print("%s Eating Shit" %self.name)
    
    def sleep(self):
        print("%s Sleeping " %self.name)
        
class Mammal(Animal):
    hasVertebrae=True
    hairedLikeC=True
    
    def doesItLikeC(self):
        print("%s Coding in C is fun and he loves it so much" %self.name)

class Neha(Mammal):
    def likesSchool(self):
        print("Neha Likes School")
    likesIndianFood = True
    
    def doesItLikeC(self):
        print("%s thinks coding in C is trash." %self.name)

#HOW MULTIPLE CLASSES CAN BE INHERITED
class Alan(Mammal):
    def likes_School(self):
        print(" Alan likes school")
    
    def loves_Python(self,bool):
        print("Alan's favorite language is Python on top of C.")

class Omar(Mammal):
    def likesJava(self, bool):
        if bool:
            print("Omar loves Java")
        else:
            print("Alan loves C")


puppy=Mammal()
dog=Mammal()
person=Mammal()
alan=Alan()

puppy.name="Eva is"
dog.name="Don Jr is an idiot and is"
person.name="Dumb Ivanka is"
alan.name="Alan thinks"
alan.doesItLikeC() 
alan.loves_Python(True)

person.sleep()
dog.eat()
puppy.sleep()

neha = Neha()
neha.name= "Neha"
neha.doesItLikeC()
omar= Omar()
omar.name="Omar"
omar.likesJava(False)
