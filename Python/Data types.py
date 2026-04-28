# Strings
# Combination of integers, letters and special characters
# Always has to be used with quotes
# For example: "Hello World"
# Or: "Hello_World123@gmail.com"

print("Hello, I am a MagicBook") # String



# Integers
# 1, 2, 3

print(1)



# Booleans
# True or False

day_when_I_am_writing_this = "Tuesday"

true_false = day_when_I_am_writing_this == "Tuesday"
print(true_false)



# Lists
# A list of strings, integers or booleans
# Is written in square brackets []

list = [] # An empty list

list2 = ["Benzin", 86, True] # A list with a string, integer and a boolean

# There are functions to work with lists

list2.append("Diesel") # Adds the string "BENZIN" to list2
list2.remove("Diesel") # Removes a certain item from list2

# A list can hold any data type, including lists
# That means we can make a list in a list

list3 = []
list4 = []

list5 = [list, list2, list3, list4]


# Dictionary
# Stores keys and values
# Is always written in wavy brackets or whatever they are called {}

# They can be written like this
dictionary = {"Name": "Nexus", "Age": 13}

# But I like to make it more clean like this
dictionary2 = {"Name": "Nexus",
               "Age": 13,
               "email": "timotej.petrik1@gmail.com",
               "phone": "+421911833299"}



