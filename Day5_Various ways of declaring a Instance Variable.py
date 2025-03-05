# Instance Variables: These are the variables that are declared inside a class or constructor.

class Demo:
    def __init__(self):  # Constructor method
        self.a = 10  # Instance variable 'a' initialized
        self.b = 15  # Instance variable 'b' initialized

    def disp(self):  # Method to display instance variables
        print(self.a)  # Printing value of 'a'
        print(self.b)  # Printing value of 'b'
        self.c = 40  # New instance variable 'c' is created inside the method
        self.d = 50  # New instance variable 'd' is created inside the method

# Creating an object of the Demo class
d1 = Demo()

# Printing instance variables initialized in the constructor
print(d1.a)  # Output: 10
print(d1.b)  # Output: 15

# Calling the disp() method, which initializes 'c' and 'd'
d1.disp()

# Creating a new instance variable 'e' outside the class
d1.e = 60

# Accessing instance variables defined inside disp()
print(d1.c)  # Output: 40
print(d1.d)  # Output: 50

# Accessing the dynamically created instance variable 'e'
print(d1.e)  # Output: 60
