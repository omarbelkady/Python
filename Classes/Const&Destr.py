print("<-----2526 56837 6342----->\nThe beginning of my prog!")
class Animal(object):
    #name static variable meaning shared throughout all the instances of the class
    name= "Not named"
    
    #I create a constructor. A constructor is called
    #Anytime we instantiate the class
    #If we do not create a constructor one is created for us by default in memory
    # We call this the default constructor
    def __init__(self):
        print("Remember this fires when we create an instance of the class. \nFYI Animal Constructed!")
        
    #A default constructor does absolute nothing. The default constructor example:
    """
        def __init__(self):
            pass
    """
myBird=Animal()
class Amphibian(Animal):
    
    beautifulScales= True #this is a static var
    def __init__(self):
        print("Just created an Amphibian for ya!")

class Mammal(Animal):
    
    aintHairless= True #this is a static var
    def __init__(self):
        super()
        print("We just created an Mammal!")

class Insect():
    hasWings= True #this is a static var
    
    def __init__(self):
        print("We just created an Insect!")
    
    #destructor is called automatically when the class is deconstructed
    def __del__(self):
        print("The insect instance of " + self.__class__.__name__ + " was just destroyed")
    
    def name(self, x):
        print("Hello Insecty your name is " + x)

firefly = Insect()
firefly.name("Samuel")
