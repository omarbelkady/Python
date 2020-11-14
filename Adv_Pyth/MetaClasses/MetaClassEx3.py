class Meta(type):
    def __new__(self, class_name, bases, attributes):
        alpha= {}
        for the_name, value in attributes.items():
            if(the_name.startswith("__")):
                alpha[the_name]=value
            else:
                alpha[the_name.upper()]=value
        return type(class_name, bases, attributes)

class Cstsffb(metaclass=Meta):
    cobfb = 2662532
    pintfb = 746867

    def sayhi(self):
        print("2526 is the biggest 27-375 32 in the world")

cfb = Cstsffb()
print(cfb.sayhi())