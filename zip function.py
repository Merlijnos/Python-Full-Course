# zip (*iterables) --> returns a zip object with tuples of all the elements of iterables
# crates a zip object with tuples of all the elements of iterables

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

usernames = ['Dumbledore', 'McGonagall', 'Hagrid', 'Snape', 'Sirius']
passwords = ('elderwand', 'transfiguration', 'dragon', 'potions', 'prongs')
login_date = ['1/1/2020', '1/2/2020', '1/3/2020', '1/4/2020', '1/5/2020']

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)
# users = dict(zip(usernames, passwords))

# print(type(users))
      
# for key,value in users.items():
#     print(key+': '+value)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------