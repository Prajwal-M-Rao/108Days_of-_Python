#A list in Python is an ordered, mutable collection of elements that can store items of different data types.
# ----------- Taking user input to build a list -----------
L = []
i = 0
while True:
    print("Enter a value: ")
    num = input()
    L.insert(i, num)  # Add element at index i
    i += 1
    print("Do you wish to continue")
    print("Press 1:Yes")
    print("Press 2:No")
    choice = int(input())
    if choice == 1:
        continue
    else:
        break
print("List: ", L)

# ----------- List Indexing and Slicing -----------
l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(l)
print(l[:-4])        # From start to 5th element
print(l[4::-1])      # Reverse from index 4 to 0
print(l[::-3])       # Every 3rd element in reverse
print(l[-5])         # 5th from last
print(l[-2:-8])      # Empty (invalid range with positive step)
# print(l[-6:-1:0])  # Error: step cannot be zero
print(l[:-8:-1])     # Reverse till second last
# print(l[-2:-8])    # No output
print(l[::])         # Full list copy
print(l[-1])         # Last element
