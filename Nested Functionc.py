# Example 1: Defining an outer function with an inner function (not called)
def outer():
    print("Inside Outer")

    def inner():
        print("Inside Inner")

# Calling only the outer function
outer()

# Example 2: Calling the inner function inside the outer function
def outer():
    print("Inside Outer")

    def inner():
        print("Inside Inner")

    inner()  # Executing the inner function

# Calling outer, which also calls inner
outer()

# Global variable
a = 10

# Example 3: Using 'nonlocal' inside a nested function
def outer():
    b = 20  # Local variable to outer()

    print("A:", a)  # Accessing the global variable
    print("B:", b)  # Printing local variable before modification

    def inner():
        nonlocal b  # Allows modification of 'b' from the outer scope
        c = 30  # Local variable to inner()
        b = 40  # Modifying 'b'

        print("C:", c)  # Printing local variable of inner
        print("A:", a)  # Accessing global variable
        print("B:", b)  # Modified value of 'b'

    inner()  # Calling the inner function
    print("B:", b)  # Checking modified 'b' after calling inner

# Calling the outer function
outer()

# Printing the global variable 'a'
print("A:", a)
