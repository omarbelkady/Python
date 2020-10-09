class Dog:
    #Default constructor
    def __init__(self):
        print("I will be printed no matter what if you instantiate me")
    def talk(self):
        print("Woof Woof")
    def walk(self):
        print("A Dog walks whilst leaving his paw signature behind")

class Cat(Dog):
    def __init__(self):
        print("Hello")
    def talk(self):
        print("Meow")
    def walk(self):
        print("A Cat walks leaving circular paw signature in contrast to oval paw of a dog")
#Creating the Cat instance
cat_obj=Cat()

#Creating the Dog instance
dog_obj=Dog()

#Looping through the Dog and Cat Methods
for anim in(cat_obj, dog_obj):
    anim.talk()
    anim.walk()

