# Classes are also used to simplify our code

# Classes have parameters and methods
# They are kind of like recipes to create objects
# For example
# I have a class named "Dog"
# I give it parameters "Name" and "Color"
# Now I can create a dog that has a certain name and color

# Methods are basically functions defined in a class

class Test: # A class named "Test"
    def TestMethod(): # A method named "TestMethod"
        pass


# The syntax when defining methods is the same as with functions
# And methods work exactly as functions
# Really they are just functions named differently


# Classes use something called a constructor

class Test2:
    def __init__(self, Number1, Number2): # Constructor
        pass

# self, Number1 and Number2 are parameters
# The "self" parameters is always present in classes and their methods
# It is kind of a "Shared" variable amongst the methods
# For example, In the constructor I type: self.Name = Name
# Now I can call self.Name in ANY of the methods in that class


# Let's make a class "Dog"

class Dog:
    def __init__(self, name, color): # Constructor, I have parameters self, Name and color
        self.name = name # I define self.name as name which I received from the constructor
        self.color = color # The same with the color

    def Bark(self): # Now I define a method "Bark"
        print(f"WOOF WOOF, My name is {self.name}") # And here I call self.name which I set to the name in the constructor

    def Speak(self):
        print(f"Hello, I am {self.color}")

