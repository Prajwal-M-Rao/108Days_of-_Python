def rev_num(num, rev, pal):
    if num <= 0:
        return rev == pal
    rem = num % 10
    return rev_num(num // 10, rev * 10 + rem, pal)

num = int(input("Enter a number: "))
if rev_num(num, 0, num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
