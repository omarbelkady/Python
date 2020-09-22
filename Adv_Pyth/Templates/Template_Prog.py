from string import Template

#Overriding the Template
class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item="PascalBook", price=1.99, qty=3))
    cart.append(dict(item="LLPResearch", price=15, qty=1))
    cart.append(dict(item="MachLang", price=0.99, qty=2))

    #Create a template and instead of dollar signs I use hashes
    my_templat = MyTemplate("#qty x #item = #price")
    total=0
    print("Cart: ")
    for the_data in cart:
        print(my_templat.substitute(the_data))
        total += the_data["price"]
    print("Total: "+str(total))

if __name__ == "__main__":
    Main()

#We use Templates because it saves us time and reduces code size
#Templates are super beneficial for webpages because they follow the same template
#but have different data within them
