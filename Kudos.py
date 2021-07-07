#global variable
alpha = 5

class Kudos:
    #constructor
    def __init__(self):
        print("This is a constructor")
        pass
   
    #class method
    def cat(self, food):
        self.food = food
        print("This cat likes to eat "+food)

    # private variable and aka local
    alpha = 6


# Creating an instance of the class
kudos = Kudos()

# Calling the class method cat on the instance
kudos.cat("fish")

#Print the local value of alpha which is 6 NOOOT 5
print("This will not get print out and error "+str(kudos.alpha))

# Print the global value of alpha which is 5 because alpha can be accessed by anyone
print(alpha)
