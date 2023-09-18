# multiple inheritance = when a child class inherits from multiple parent classes

class Prey:
    def flee(self):
        print("This prey is fleeing.")

class Predator:
    def hunt(self):
        print("This predator is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()