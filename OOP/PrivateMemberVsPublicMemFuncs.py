class EnjoysToCodeInAssembly:
    def __init__(self, name):
        #public member variable
        self.pasc="Pascal"
        self.pintos="Pintos"
        self.assm="Assembly"
    def public_method(self):
        print("This is a a public method")
        #assm, pintos and pasc are private member variables
        self.assm
        #How to call a private method must use self keyword
        self.__llpenthusiast()
    
    #private member function
    def __llpenthusiast(self):
        print("A private method")

thepasclover=EnjoysToCodeInAssembly("LLPLover")
thepasclover.public_method()

#this will error because it is a private method
#thepasclover.__llpenthusiast()