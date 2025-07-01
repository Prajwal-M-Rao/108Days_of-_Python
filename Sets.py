# ---------------------- SET OPERATIONS IN PYTHON ----------------------

# Creating and printing a set
s = {10, 20, 40, 50, 30, 5}
print("Original Set:", s)  # Sets are unordered and unique
print("Type of s:", type(s))

# Note: Sets do not support indexing like lists or tuples
# print(s[0])  # ❌ This would raise a TypeError

# ---------------------- TRAVERSING A SET ----------------------

print("\nTraversing the set using enumerate:")
for index, value in enumerate(s):
    print("Index:", index, "Value:", value)

# ---------------------- ADDING AND REMOVING ELEMENTS ----------------------

# Creating an empty set
a = set()

# Taking 5 elements as input from the user
for i in range(5):
    num = int(input("Enter a value to add to the set: "))
    a.add(num)  # Adds the value to the set
print("User-entered set:", a)

# Adding multiple elements using update()
a.update([50, 60, 70])
print("Set after update:", a)

# Removing element using discard() (no error if element doesn't exist)
dele = int(input("Enter a value to discard from the set: "))
a.discard(dele)
print("Set after discard:", a)

# Removing element using remove() (raises error if element doesn't exist)
try:
    a.remove(60)
    print("Set after removing 60:", a)
except KeyError:
    print("Value 60 not found in the set. Cannot remove.")

# ---------------------- FROZENSET (IMMUTABLE SET) ----------------------

s = {10, 20, 30, 40, 50}
frozen = frozenset(s)
print("\nFrozen Set:", frozen)

# The following operations are not allowed on frozenset
# frozen.add(90)     ❌ Error: frozenset is immutable
# frozen.remove(10)  ❌ Error: frozenset is immutable

# ---------------------- IMMUTABLE VS MUTABLE ELEMENTS ----------------------

# Invalid set: sets cannot contain mutable types like another set
# s1 = {10, 20, 30, {1, 2}}  # ❌ TypeError

# Valid set with a tuple (immutable)
s1 = {10, 20, 30, (1, 2)}
print("Valid set with a tuple:", s1)
