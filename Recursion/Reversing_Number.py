def rev_num(num, rev):
    if num <= 0:
        return rev
    rem = num % 10
    return rev_num(num // 10, rev * 10 + rem)

num = int(input("Enter a number: "))
print("Reversal of", num, "is", rev_num(num, 0))
