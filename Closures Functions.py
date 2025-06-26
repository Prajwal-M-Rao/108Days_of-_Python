#A closure in Python is a function that captures the variables from its enclosing scope and remembers them even after the outer function has finished execution.

def outer():
    print("Inside Outer ")
    def inner():
        print("Inside Inner")
    return inner  # Returning the inner function reference

ref = outer()  # Call outer() and store the returned function reference
print(ref)  # Prints the reference of the inner function
ref()  # Calls the inner function

# Detailed explaination in pdf
