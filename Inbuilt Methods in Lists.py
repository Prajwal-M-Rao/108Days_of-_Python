a = [10, 20, 30, 40, 50]
print(a)                  # Output: [10, 20, 30, 40, 50]


#  .insert(index, value):  Adds an element at a specific index without replacing the existing element.
a.insert(2, 25)           # Insert 25 at index 2 → [10, 20, 25, 30, 40, 50]
a.insert(3, 32)           # Insert 32 at index 3 → [10, 20, 25, 32, 30, 40, 50]
print(a)


#.append(value): Adds an element to the end of the list.
a.append(70)
a.append(90)
print(a)                  # Now → [10, 20, 25, 32, 30, 40, 50, 70, 90]


#.extend(iterable): Adds multiple elements from another iterable (e.g., list) to the end.
a.extend([90, 100, 110])
print(a)                  # Now → [10, 20, 25, 32, 30, 40, 50, 70, 90, 90, 100, 110]


#.remove(value): Removes the first occurrence of a specific value.
a.remove(50)
print(a)                  # Removes 50 (only the first one if duplicates exist)


#.pop(): Removes and returns the last element (or element at given index).
a.pop()                   # Removes 110 (last element)
print(a)

a.pop(3)                  # Removes element at index 3 → 32
print(a)


#.clear(): Removes all elements from the list (list becomes empty).
a.clear()
print(a)                  # Output: []


#del a: Deletes the entire list from memory.
del a                    # Now 'a' no longer exists
