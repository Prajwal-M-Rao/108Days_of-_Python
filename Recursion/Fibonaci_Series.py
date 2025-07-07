def fibonacci(n1, n2, pos):
    if pos <= 0:
        return
    print(n1, end=' ')
    fibonacci(n2, n1 + n2, pos - 1)

pos = int(input("Enter the number of terms: "))
fibonacci(0, 1, pos)
