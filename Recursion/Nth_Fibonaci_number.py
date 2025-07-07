def nth_fib(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return nth_fib(pos - 1) + nth_fib(pos - 2)

pos = int(input("Enter the position: "))
print("The Fibonacci number at position", pos, "is", nth_fib(pos))
