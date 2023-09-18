from car import Car

car_1 = Car("BMW", "M4", 2022, "Grey")
car_2 = Car("AUDI", "RS6", 2021, "Black")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_1.stop()