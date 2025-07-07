def fact(num):
    if num == 1:
        return 1
    return num * fact(num - 1)

num = int(input("Enter a number: "))
if num <= 0:
    print("Enter a positive number")
else:
    print("The factorial of", num, "is", fact(num))
