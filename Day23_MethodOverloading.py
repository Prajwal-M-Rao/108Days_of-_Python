#Function overloading is a feature where multiple functions with the same name can have different implementations based on the number or type of arguments passed.

def fun1():
    print("P")
def fun1():
    print("J")
def fun1():
    print("Z")
fun1()

# The first two fun1 definitions are overridden.
# Only the last definition (print("Z")) remains.

def fun2(a):
    print("1")
def fun2(a,b):
    print("2")
def fun2(a,b,c):
    print("3")
fun2(10)

# Similar to the first part, the last definition of fun1(a,b,c) overrides the previous ones. 
# When calling fun1(10), Python expects fun1 to take three arguments (a, b, c). 
# Since fun1(10) provides only one argument, Python raises a TypeError 
