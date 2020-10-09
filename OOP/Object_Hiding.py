class Fav_Subjs:
    __hiddenVar = 'C#, Python and Javascript are awesome prog langs'

    #class method that alters __hiddenVar
    def change(self, appending):
        self.__hiddenVar += appending
        print(self.__hiddenVar)

#instantiating a object/Creating an instance of the class
newObject = Fav_Subjs()

#Calling the change class method
newObject.change(" and T Swift")
newObject.change("!!!!!!!!!!")

objectNumber2 = Fav_Subjs()
#To access hidden Class members we use an undersquare right before the class Name
print(objectNumber2._Fav_Subjs__hiddenVar)
