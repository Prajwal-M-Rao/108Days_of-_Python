# A tuple is an ordered, immutable collection in Python that allows duplicates and is defined using ().

# Creating 1D, 2D, and 3D tuples
t1 = (10, 20, 30, (1.1, 2.2, ('a', 'b'), 3.3), 40, 50, (4.4, 5.5, ('c', 'd'), 6.6), 60)

print("Length of t1:", len(t1))        # Length of top-level tuple
print("3rd element (1D):", t1[2])      # Simple element (1D)

# 2D access
print("4th element is a 2D tuple:", t1[3])       # Entire 2D tuple
print("Element at t1[3][1] (2D):", t1[3][1])     # 2.2 from 2D tuple
print("Element at t1[6][0] (2D):", t1[6][0])     # 4.4 from another 2D tuple

# 3D access
print("Element at t1[3][2] (3D sub-tuple):", t1[3][2])    # ('a', 'b')
print("Element at t1[3][2][0] (3D):", t1[3][2][0])        # 'a'
print("Element at t1[6][2][1] (3D):", t1[6][2][1])        # 'd'

# More access examples
print("Last element (1D):", t1[-1])          # 60
print("Nested float value (2D):", t1[6][3])  # 6.6
print("Nested character (3D):", t1[6][2][0]) # 'c'
