# students = ["squidward", "sandy", "patrick", "mr.krabs", "plankton", "gary"]

# # students.sort(reverse=True)
# sorted_students = sorted(students, reverse=True)

# for i in sorted_students:
#     print(i) 


# Harder part of the exercise

students = [("Squidward", "E", 50),
            ("Sandy", "A", 33),
            ("Patrick", "D", 29),
            ("Mr. Krabs", "B", 77),
            ("Plankton", "C", 55),]

age = lambda ages:ages[2]
# students.sort(key=age, reverse=True)
sorted_students = sorted(students, key=age)

for i in students:
    print(i)