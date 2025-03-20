#Decorators
def outer1(function):
    print("Inside Outer")
    def inner1():
        print("Inside inner")
    return inner1

def print_msg():
    print("Hiiii")

def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering Inner")
        ref=print1
        ref()
        print("Leaving inner")
    return inner

ptr1=print_msg
ptr2=outer(ptr1)
ptr2()
print("End of Program")
print("\n\n")

#converting the string to upper using decorator

def print_msg():
    return "Hiiii Everyone"  # Return string instead of printing

def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering Inner")
        ref = print1  # Function reference
        str1 = ref()  # Call function and get the returned string
        str2 = str1.upper()  # Convert string to uppercase
        print(str2)  # Print the modified string
        print("Leaving inner")
    return inner  # Return the inner function

ptr1 = print_msg  # Assign print_msg function to ptr1
ptr2 = outer(ptr1)  # Call outer() with ptr1, getting inner() function
ptr2()  # Execute inner function

print("End of Program")