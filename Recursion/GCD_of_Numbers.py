def gcd_of_numbers(n1, n2, hcf, i):
    if i > n1:
        return hcf
    if n1 % i == 0 and n2 % i == 0:
        hcf = i
    return gcd_of_numbers(n1, n2, hcf, i + 1)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    n1, n2 = n2, n1

print("The HCF is", gcd_of_numbers(n1, n2, 0, 1))
