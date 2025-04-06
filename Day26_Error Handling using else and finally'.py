# --------------------- using else block --------------------

print("Pgm started")
try:
    c = 10 / 2  # Division succeeds
    print(c)
except Exception as e:
    print("Error!!")
else:
    print("Pgm end")  # Runs only if no exception occurs


# --------------------- using finally block -----------------

def fun1():
    print("Entering fun1")
    try:
        fun2()  # Call fun2 which contains try-except-finally
    except Exception as e:
        print("Error!! in fun1")
        raise e  # Re-raise to handle in main
    finally:
        print("Finally block in fun1")  # Always runs
    print("Leaving fun1")

def fun2():
    print("Entering fun2")
    try:
        res = 10 / 0  # Will raise ZeroDivisionError
        print(res)
    except Exception as e:
        print("Error! in fun2")
        raise e
    finally:
        print("Finally block in fun2")  # Always runs
    print("Leaving fun2")

print("Pgm startred")
try:
    fun1()  # fun1 calls fun2
except Exception as e:
    print("Error!!! in main")  # Final error handler
print("Pgm end")
