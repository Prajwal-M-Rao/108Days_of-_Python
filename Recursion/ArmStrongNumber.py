def dig_count(num, count):
    if num <= 0:
        return count
    return dig_count(num // 10, count + 1)

def is_ASN(num, asn, pow, temp):
    if num <= 0:
        return temp == asn
    base = num % 10
    asn += base ** pow
    return is_ASN(num // 10, asn, pow, temp)

num = int(input("Enter a number: "))
pow = dig_count(num, 0)
flag = is_ASN(num, 0, pow, num)
if flag:
    print(num, "is an ASN")
else:
    print(num, "is not an ASN")
