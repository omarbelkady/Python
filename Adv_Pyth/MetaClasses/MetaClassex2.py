#Using Metaclasses With Inheritance
class FavOS:
    def theBestOperatingSys(self):
        print("CS375FB: Pintos")
def favClassAtUT(self):
    self.bestProg="Pascal Programming"

#How To Inherit: InherittedClass Will Now Inherit From FavOS  AND HOW TO APPREND A FUNCTION TO THE CLASS
InheritedClass=type("InheritedClass", (FavOS,), {"bestCourse": "CS375", "favClass":favClassAtUT})
c = InheritedClass()
c.theBestOperatingSys()
# How To Use A Function That is Outside a Class
c.favClass()
print("This was the best skill I ever learned at UT: "+str(c.bestProg))