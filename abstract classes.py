#abstract classes = a class which contains one or more abstract methods
# abstract method = a method that is declared in the parent class but has no implementation
# abstract classes cannot be instantiated and require subclasses to provide implementations for the abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop (self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car.")

    def stop(self):
        print("You stop the car.")

class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle.")

    def stop(self):
        print("You stop the motorcycle.")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

# vehicle.stop()
car.stop()
motorcycle.stop()
