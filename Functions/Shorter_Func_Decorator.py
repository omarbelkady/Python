def Nelan_And_C(assembly):
    #nested func
    def adding_functionality(TSwift):
        return "He loves "+assembly(TSwift)
    
    #decorator example
    return adding_functionality

@Nelan_And_C
def printing(inp):
    return inp
print(printing("Taylor Swift and \t Low-Level!!!!!!!!!!"))
