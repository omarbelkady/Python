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

assemblylov3r= IsALLPLov3R("CDeveloper", "Nelan")
lllover = IsALLPLov3R("Assembly", "6342_56837")
print(assemblylov3r.title)
#print(assemblylov3r.is_Nelan)
IsALLPLov3R.fav_proglangs.append(assemblylov3r)
IsALLPLov3R.fav_proglangs.append(lllover)
for c in IsALLPLov3R.fav_proglangs:
    print(c.title, c.name)
