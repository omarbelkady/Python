class Person(object):
    
    #What exactly is an Object my Friend:
        #An object is simply a bank of variables and functions
        #A class is the architect of the object
        #Objects and instances of class are interchangeable
        # When we create an object it called instantiating.
        #self is a reference to the current object
    def name(self, args):
        print("My name is "+ args)
    def occupation(self,args):
        print("and my occupations are",args)
        
    #def hobbies(self,args):
    #   print(args)
    
    likes2Read=False
    
    
    
class Robert(Person):#Robert is a derived class of Person
    def educated(self):
        print("Robert is educated!")
    
    #how to override
    likes2Read = True

Richard = Person()
Richard.name("Richard")
Richard.occupation("programmer and doctor")
Roberto = Robert()
Roberto.name("Roberto ")
Robert.educated("isn't")


