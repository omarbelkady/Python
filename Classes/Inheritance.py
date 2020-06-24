class Parent():
    def print_last_name(self):
        print("Belkady")
class Child(Parent):
#the parent argument is how to inherit
    def print_first_name(self):
        print('Omar')
        
youssef=Child()
youssef.print_first_name()
youssef.print_last_name()

