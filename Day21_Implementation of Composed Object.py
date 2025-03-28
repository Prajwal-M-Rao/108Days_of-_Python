'''
A composed object in Python refers to an instance of a class that is embedded within another class through composition.
Composition is an OOP principle where one class contains an instance of another class, creating a "has-a" relationship rather than an "is-a" relationship (which is used in inheritance)
'''

# Class representing an Operating System
class OS:
    def __init__(self):
        self.status = True  # OS status attribute
        print("OS is installed")

    def getOS(self):
        print("OS is still installing")  # Method to display OS status

# Class representing a Mobile device
class Mobile:
    def __init__(self, name):
        self.mname = name  # Mobile name attribute
        self.o = OS()  # Creating an instance of OS inside Mobile (Composition)
        print("Mobile is ready")
        print("with OS")

# Creating a Mobile object (which also creates an OS object)
m = Mobile("iPhone")

# Printing the mobile name
print(m.mname)  # Output: iPhone

# Accessing the composed object (OS) and printing its status
print(m.o.status)  # Output: True

# Calling a method from the composed object (OS)
m.o.getOS()  # Output: OS is still installing
