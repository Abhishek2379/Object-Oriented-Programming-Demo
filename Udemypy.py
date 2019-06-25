
###python3
##class Car:
##    pass

class  Car(object):
    #Class attribute
    engine="Volkswagen"

    def __init__(self,make,model,fuel):
        #Instance attributes
        self.make=make
        self.model=model
        self.fuel=fuel

    #Define some instance methods
    def start(self):
        print("The car is started!!")
    def  changeMake(self,make):
        self.make=make;
    def stop(self):
        print("The car is stopping!!")
    def brake(self):
        print("The car is braking!!")
    #instance method with arguments
    def honk(self,sound):
        print("The car is honking",sound)

#Objects
car1 = Car("Mahindra","2008","Diesel")
car2 = Car("Audi","2019","Diesel")

#calling methods
car1.start()
car1.stop()
car1.brake()

#calling instance methods
car1.honk("beep")
car2.honk("Love the way you are")



print("{} and {} and {}".format(car1.make, car1.model, car1.fuel))

car1.changeMake("BMW")
print("{} and {} and {}".format(car1.make, car1.model, car1.fuel))

#print instance  attributes

##print("The make of Car 1 is",car1.make)
##print("The model of Car 1 is ",car1.model)
##print("The fuel type of Car 1 is",car1.fuel)
##
##print("The make of Car 12 is",car2.make)
##print("The model of Car 2 is ",car2.model)
##print("The fuel type of Car 2 is",car2.fuel)
##
###print class attributes
##print("The Engine manufacturer  of Car 1 is",car1.engine)
##print("The Engine manufacturer  of Car 2 is",car2.engine)



#if you update class attribute for one object it doesnt affect the other object

#what do child classes inherit from parent classes
#Attributes
#Behaviours or methods
