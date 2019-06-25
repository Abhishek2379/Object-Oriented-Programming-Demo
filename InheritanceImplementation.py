class Car(object):
    
    

    def __init__(self,make,model,fuel):
        #Instance attributes
        self.make=make
        self.model=model
        self.fuel=fuel

    #Define some instance methods
    def start(self):
        print("The car is started!!")
    def stop(self):
        print("The car is stopping!!")
    def brake(self):
        print("The car is braking!!")

#Mahindra sub-class
class Mahindra(Car):
    def mode4and4(self):
        print("4x4 activated!!")
        return

#Audi sub-class
class Audi(Car):
    def sportsmode(self):
        print("Sports mode activated")
        return 

mahindra1 =Mahindra("Mahindra","2019","Diesel")
mahindra1.mode4and4()
audi1=Audi("Audi","2019","Diesel")
audi1.sportsmode()
#invoking start method on Mahindra and Audi cars
mahindra1.start()
audi1.start()
