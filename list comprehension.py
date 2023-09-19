# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

squares = [] # empty list
for i in range(1, 11): # for loop
    squares.append(i*i)  # append() method adds an item to the end of the list
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = [i*i for i in range(1, 11)] # list comprehension
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]