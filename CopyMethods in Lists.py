a = [10, 20, 30, 40, 50]

# Shallow Copy (both a and a1 refer to the same object)
a1 = a
print(a1)            # Output: [10, 20, 30, 40, 50]

a[3] = 80
print(a)             # Output: [10, 20, 30, 80, 50]
print(a1)            # Output: [10, 20, 30, 80, 50] -> reflects change in 'a'

print("\n")

# Deep Copy (copy() creates a new list with same values)
b1 = a.copy()
print(b1)            # Output: [10, 20, 30, 80, 50]

del a[3]             # Remove element at index 3 (80)
print(a)             # Output: [10, 20, 30, 50]
print(a1)            # Output: [10, 20, 30, 50]  -> still same as 'a'
print(b1)            # Output: [10, 20, 30, 80, 50] -> unaffected
