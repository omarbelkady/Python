#a decorator is a function that takes another function as input and extends
#the behavior of the inputted function without deliberately modifying it
def messageGreeting(str):
    #ex. of a nested func aka a func within a func
    def another_MsgGreeting():
        return "Nelan Loves: "

    #concatenating another_MsgGreeting to what we passed in to the func call of messageGreeting
    return another_MsgGreeting() + str

def things_he_loves(elems):
    return elems

print(messageGreeting(things_he_loves("Taylor Swift and C all day everyday")))
