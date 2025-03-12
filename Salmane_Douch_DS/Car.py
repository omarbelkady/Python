class CAR:
    def __init__(self,brand,model,color, speed):
        self.brand=brand
        self.model=model
        self.color=color
        self.speed=speed
    def __str__(self):
        return("The brand is "+str(self.brand)+" and the model is: " +str(self.model)+" and the color is: " +str(self.color)+" and it is speed: "+str(self.speed))

ahmed_car = CAR("BMW", "5 series", "Red", 58)
print(ahmed_car)