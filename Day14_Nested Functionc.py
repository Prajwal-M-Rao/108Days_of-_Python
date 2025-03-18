# Defining the outer function
def outer():
    print("Inside Outer")  # Prints a message when outer() is called

    # Defining an inner function but not calling it
    def inner():
        print("Inside Inner")  # This function prints a message when called


# Calling the outer function (Note: inner() is not executed)
outer()


# Defining the outer function again
def outer():
    print("Inside Outer")  # Prints a message when outer() is called

    # Defining the inner function
    def inner():
        print("Inside Inner")  # This function prints a message when called

    inner()  # Calling the inner function inside the outer function


# Calling the outer function, which will also execute inner()
outer()

# Global variable
a = 10


# Defining the outer function
def outer():
    b = 20  # Local variable in outer(), but will be modified using nonlocal

    print("A:", a)  # Accessing the global variable 'a'
    print("B:", b)  # Printing local variable 'b' before modification

    # Defining the inner function
    def inner():
        nonlocal b  # Declaring 'b' as nonlocal to modify it in outer()
        c = 30  # Local variable to inner()
        b = 40  # Modifying 'b', which is nonlocal (belongs to outer())

        print("C:", c)  # Printi#A nested function is a function that is defined inside another function.

# Outer function definition
def outer():
    print("Inside Outer")

    # Inner function defined but not called
    def inner():
        print("Inside Inner")


# Calling outer function (inner is not executed)
outer()


# Outer function with inner function being called
def outer():
    print("Inside Outer")

    def inner():
        print("Inside Inner")

    inner()  # Calling inner function


outer()

# Global variable
a = 10


def outer():
    b = 20  # Local variable

    print("A:", a)  # Accessing global variable
    print("B:", b)  # Printing local variable before modification

    def inner():
        nonlocal b  # Allows modification of b in outer function
        c = 30  # Local to inner()
        b = 40  # Modifying b

        print("C:", c)
        print("A:", a)
        print("B:", b)  # Modified value of b

    inner()
    print("B:", b)  # Checking modified b


outer()

print("A:", a)  # Printing global variable
ng local variable 'c'
        print("A:", a)  # Accessing the global variable 'a'
        print("B:", b)  # Printing modified value of 'b'

    print("B:", b)  # Printing 'b' before calling inner()
    inner()  # Calling the inner function
    print("B:", b)  # Printing 'b' after modification in inner()


# Calling the outer function
outer()

# Printing global variable 'a'
print("A:", a)
