def fun1():
    print("Entering fun1")
    try:
        fun2()  # Call function that may raise an error
    except Exception as e:
        print("Error in fun1")  # Handle any exception from fun2
    print("Leaving fun1")

def fun2():
    print("Entering fun2")
    res = 10 / 0  # This will cause ZeroDivisionError
    print(res)
    print("Leaving fun2")

print("Pgm startred")  # Program starts
fun1()                 # Call main function
print("Pgm end")       # Program ends
