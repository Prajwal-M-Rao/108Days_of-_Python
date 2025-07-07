def sum_num(num):
    if num == 0:
        return 0
    return num + sum_num(num - 1)

num = int(input("Enter a number: "))
print("The sum of first", num, "natural numbers is", sum_num(num))
