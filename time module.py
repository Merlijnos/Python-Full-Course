import time

# print(time.ctime(0)) # convert a time expressed in seconds since the epoch to a string representing local time
# # epoch = when you computer was born



# # print(time.time()) # returns the current time in seconds since the epoch

# print(time.time()) # returns the current time in seconds since the epoch

# print(time.ctime(time.time())) # convert a time expressed in seconds since the epoch to a string representing local time

# time_object = time.localtime() # convert a time expressed in seconds since the epoch to a struct_time in local time
# print(time_object)

# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) # convert a time object to a string according to a given format
# print(local_time)

# time_object = time.gmtime() # convert a time expressed in seconds since the epoch to a struct_time in UTC

# time_string = "21 June, 2018"
# time_object = time.strptime(time_string, "%d %B, %Y") # convert a string to a time object according to a given format
# print(time_object)

time_tuple = (2020, 4, 18, 3, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # convert a time tuple to a string representing local time
print(time_string)