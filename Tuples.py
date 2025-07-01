# A tuple is an ordered, immutable collection in Python that allows duplicates and is defined using ().

# Creating a tuple with multiple elements
t1 = (10, 20, 30)
print(type(t1))  # <class 'tuple'> - It's a tuple

# Creating a tuple with a single element (important syntax)
t2 = (10)        # This is NOT a tuple, just an integer in parentheses
print(type(t2))  # <class 'int'>

# Correct way to define a single-element tuple is:
# t2 = (10,)  --> with a comma

# Another tuple with multiple elements
t3 = (10, 20, 30, 40, 50, 60, 70, 80, 90)

# Length of the tuple
print(len(t3))  # 9

# Checking type
print(type(t3))  # <class 'tuple'>

# Accessing elements
print(t3[0])      # First element: 10
print(t3[1:4])    # Slicing: 2nd to 4th elements (index 1 to 3): (20, 30, 40)
print(t3[-1])     # Last element: 90
print(t3[4:])     # Elements from index 4 to end: (50, 60, 70, 80, 90)

# Slicing with range
print(t3[-8:-2:1])  # Elements from 2nd to 7th (indexes 1 to 6): (20, 30, 40, 50, 60, 70)
print(t3[:3:-1])    # From last element to index 3 (not including index 3): (90, 80, 70, 60, 50)
print(t3[::-1])     # Reverses the entire tuple
print(t3[8:2:-1])   # From index 8 to index 3 (not including 2): (90, 80, 70, 60, 50, 40)



# How to add a new value in a tuple at a required position (tuples are immutable, so we create a new one)
a = (10, 20, 30, 40, 50)
b = a[0:2] + (25,) + a[2:]  # Inserting 25 after index 1
print(b)                   # Output: (10, 20, 25, 30, 40, 50)


# How to remove a value from a tuple (again, by creating a new one)
print(a)                   # Original tuple: (10, 20, 30, 40, 50)
c = a[0:2] + a[3:]         # Removing value at index 2 (30)
print(c)                   # Output: (10, 20, 40, 50)
