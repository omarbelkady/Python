class Parent():
  def print_last_name(self):
    print('Jackson')
class Child(Parent):
  #the parent argument is how to inherit
    def print_first_name(self):
        print('Lance')
    def print_last_name(self): #how to override the print_last_name function
	    print("Belkady")
        
gabriel=Child()
gabriel.print_first_name()
gabriel.print_last_name()
