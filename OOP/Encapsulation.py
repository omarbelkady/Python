class Clover:
    def __init__(self, favLang, favParad,favHobby):
        self.favLang=favLang
        self.favParad=favParad
        self.favHobby=favHobby
        print("Constructor called")
    
    def set_favHobby(self,val):
        self.favHobby=val
    
    def get_favHobby(self):
        return self.favHobby

nelan=Clover("Clover","Imperative","Coding in Pascal")
assembly_enthusiast=Clover("Assembly","Procedural", "Coding In Assembly")
compilers_lover=Clover("CS375FB","Pintos","Studying his Favorite Course CS375")
java_lover=Clover("Java","Object Oriented Programming")

#To change the value
#java_lover.favLang="C"

#I want to prevent line 19 from happening

class sayHi:
    def __init__(self,name):
        self.a=256837
        #private member variable too but mutable and accessible
        self._b=727225

        #private member variable not mutable nor accessible
        self.__c=746767
    def set_c(self, val):
        self.__c=val

    def get_c(self):
        return self.__c
