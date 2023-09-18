class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("You are driving the " + self.make + " " + self.model + ".")

    def stop(self):
        print("You have stopped the " + self.make + " " + self.model + ".")