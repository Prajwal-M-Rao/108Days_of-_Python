# Global and Local Variables
a = 111  # Global variable

def fun1():
    print("Global a in fun1:", a)  # Accessing global variable
    b = 22
    print("Local b in fun1:", b)

def fun2():
    print("Global a in fun2:", a)  # Accessing global variable
    c = 33
    print("Local c in fun2:", c)

print("Initial global a:", a)  # Prints global `a`
fun1()
fun2()
print("Final global a after fun1 and fun2:", a)  # Global `a` remains unchanged

# Modifying Global Variables
a = 999  # Reassigning the global variable
print("\n")
def fun3():
    global a
    a = 888  # Modifies global `a`
    b = 777
    print("Updated global a in fun3:", a)
    print("Local b in fun3:", b)

def fun4():
    global a
    a = 666  # Modifies global `a`
    c = 555
    print("Updated global a in fun4:", a)
    print("Local c in fun4:", c)

print("Initial global a before modifications:", a)  # Prints initial value (999)
fun3()    # Changes `a` to 888
fun4()    # Changes `a` to 666
print("Final global a after fun3 and fun4:", a)  # Final value of `a` after modifications
print("\n")

def funa():
    print("Inside the function")

def funb(x, y):
    z = x * y
    print("Res is", z)

def disp(ptr3, ptr4):  # Accepting functions as parameters
    ptr3()  # Calling fun1()
    ptr4(20, 20)  # Calling fun2(x, y)

funa()
a, b = 10, 5
funb(a, b)

ptr1 = funa
ptr2 = funb

ptr1()
ptr2(10, 10)

disp(ptr1, ptr2)  # Passing functions as arguments
