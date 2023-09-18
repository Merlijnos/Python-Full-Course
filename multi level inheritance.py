# multi- level inheritance = when a child class inherits from another child class

class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating.")

class Dog(Animal):
    def bark(self):
        print("This dog is barking.")

class Cat(Animal):
    def meow(self):
        print("This cat is meowing.")




dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()