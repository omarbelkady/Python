class IsALLPLov3R():
    #class level Variable
    fav_proglangs= []


    #default constructor
    def __init__(self,title, name):
        self.title=title
        self.name=name

    def is_Nelan(self):
        if(self.name == "Nelan"):
            return True
        return False

    def __str__(self):
        return f"{self.title} aka Alan Ngo\'s real name is 63526 The 746867 56837"

assemblylov3r= IsALLPLov3R("CDeveloper", "Nelan")
assemblylov3r2= IsALLPLov3R("CDeveloper", "Nelan")
lllover = IsALLPLov3R("Assembly Developer", "6342_56837")
print(assemblylov3r.title)
#print(assemblylov3r.is_Nelan)
IsALLPLov3R.fav_proglangs.append(assemblylov3r)
IsALLPLov3R.fav_proglangs.append(lllover)
for c in IsALLPLov3R.fav_proglangs:
    print(c)


#both these objects have the same data but not the same id
print(id(assemblylov3r), id(assemblylov3r2))

#prints false
print(assemblylov3r is assemblylov3r2)

#Now if I did this I would have the same id but not the same address in memory
assemblylov3r = assemblylov3r2

#prints true
print(assemblylov3r is assemblylov3r2)


#A function that changes the data of an object sample
def changeTitle(llplover):
    print(id(llplover))
    llplover.title = "Low Level Lover"
    print(id(llplover))

changeTitle(assemblylov3r)
print(assemblylov3r)
