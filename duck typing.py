# duck typing = if it walks like a duck and quacks like a duck, then it must be a duck 
# duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines.

class Duck:

    def walk(self):
        print("This duck is walking.")

    def talk(self):
        print("This duck is quacking.")

class Chicken:

    def walk(self):
        print("This chicken is walking.")

    def talk(self):
        print("This chicken is clucking.")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)