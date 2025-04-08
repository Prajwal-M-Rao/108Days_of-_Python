#all() function:
            #Returns True only if all elements in the list are truthy (non-zero).
            #If any element is 0, it returns False.
a = [10, 20, 30, 40, 50]
print(a)                   # Prints the list as-is
print(len(a))              # Length of the list: 5
print(min(a))              # Minimum value: 10
print(max(a))              # Maximum value: 50
print(all(a))              # True - because all elements are non-zero (truthy)


#any() function:
            #Returns True if at least one element is truthy.
            #Returns False only if all elements are 0 or False.
b = [10, 0, 30, 40, 50]
print(b)
print(all(b))              # False - because of the 0
print(any(b))              # True - at least one element is non-zero
c = [0, 0, 0, 0, 0]
print(all(c))              # False - all are 0
print(any(c))              # False - no truthy values


#sorted() function:
            #Returns a new sorted list (doesn’t change the original list).
            #You can use reverse=True for descending order.
d = [10, 6, 25, 1, 15]
print(sorted(d))           # Ascending: [1, 6, 10, 15, 25]
print(sorted(d, reverse=True))  # Descending: [25, 15, 10, 6, 1]
