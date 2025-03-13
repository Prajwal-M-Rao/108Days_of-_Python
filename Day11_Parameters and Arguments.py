# Define a class named Demo
class Demo:
    def swap(self, a, b):
        """
        Method to swap two values.
        Parameters:
        a (int): First value
        b (int): Second value

        Returns:
        tuple: Swapped values (b, a)
        """
        # Formal Parameters: 'a' and 'b' are the parameters of this method.
        temp = a  # Store value of 'a' in 'temp'
        a = b  # Assign 'b' to 'a'
        b = temp  # Assign 'temp' (original 'a') to 'b'
        return a, b  # Return swapped values

# Create an instance of the class Demo
d1 = Demo()

# Initialize two variables
a = 10
b = 20

# Print original values before swapping
print("Before Swapping:")
print("a =", a)
print("b =", b)

# Actual Parameters: Here, 'a' and 'b' are passed as arguments to the method.
c, d = d1.swap(a, b)

# Print swapped values
print("\nAfter Swapping:")
print("a =", c)
print("b =", d)

print("\n---------------------------\n")

# Define another class Demo (reusing the name for demonstration)
class Demo:
    def disp(self, x=11, y=22, z=33):
        """
        Method to display three values.
        Parameters:
        x (int, optional): First value, default is 11
        y (int, optional): Second value, default is 22
        z (int, optional): Third value, default is 33
        """
        # Default Arguments: If no values are provided, the function uses the default values.
        print("x =", x)
        print("y =", y)
        print("z =", z)

# Create an instance of the class Demo
d1 = Demo()

# Initialize some variables
a = 10
b = 20
c = 30

# Function calls with different types of arguments
print("Calling disp with all three arguments:")
d1.disp(a, b, c)  # Passing all arguments (Positional Arguments)
print("\n")

print("Calling disp with one argument (a), others take default values:")
d1.disp(a)  # Passing only one argument; y and z will take default values
print("\n")

print("Calling disp with no arguments, default values are used:")
d1.disp()  # Using default values for all parameters
print("\n")

print("Calling disp with one argument (c), others take default values:")
d1.disp(c)  # Only 'x' gets assigned 'c', while y and z use default values
print("\n")

print("Calling disp with two arguments (b, c), z takes default value:")
d1.disp(b, c)  # First two values assigned; z takes the default value
print("\n")

print("Calling disp using keyword argument (z=c), x and y take default values:")
d1.disp(z=c)  # Using keyword argument for z; x and y use defaults
print("\n")

print("Calling disp using keyword arguments (y=b, z=c), x takes default value:")
d1.disp(y=b, z=c)  # Specifying values for y and z using keyword arguments
print("\n")
