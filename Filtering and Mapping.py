"""
Python Script: Demonstrating Mapping and Filtering

This script covers:
1. Mapping: Applying a function to all elements in an iterable using `map()`.
2. Filtering: Selecting elements based on a condition using `filter()`.
"""

# Example 1: Using map() to double numbers
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))

print("Original Numbers:", numbers)
print("Doubled Numbers (Using map()):", doubled_numbers)

# Example 2: Using filter() to get even numbers
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))

print("Even Numbers (Using filter()):", even_numbers)

# Example 3: Combining map() and filter()
# Squaring only even numbers
squared_evens = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print("Squared Even Numbers (Using filter() + map()):", squared_evens)

# Example 4: Achieving the same result with List Comprehension
doubled_numbers_lc = [x * 2 for x in numbers]
even_numbers_lc = [x for x in numbers if x % 2 == 0]
squared_evens_lc = [x ** 2 for x in numbers if x % 2 == 0]

print("\nUsing List Comprehension:")
print("Doubled Numbers:", doubled_numbers_lc)
print("Even Numbers:", even_numbers_lc)
print("Squared Even Numbers:", squared_evens_lc)
