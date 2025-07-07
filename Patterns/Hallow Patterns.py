def hollow_square(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def square_with_diagonals(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n or j == 1 or j == n or i == j or (i + j == n + 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def top_bottom_diagonals(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n or i == j or (i + j == n + 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def left_right_diagonals(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == 1 or j == n or i == j or (i + j == n + 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def l_shape_with_diagonal(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == n or j == 1 or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def reverse_l_with_diagonal(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or j == n or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def top_left_with_anti_diagonal(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or j == 1 or (i + j == n + 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Menu
print("Choose a Hollow Pattern:")
print("1. Hollow Square")
print("2. Square with Diagonals")
print("3. Top & Bottom Borders with Diagonals")
print("4. Left & Right Borders with Diagonals")
print("5. L-shape with Diagonal")
print("6. Reverse L with Diagonal")
print("7. Top & Left Borders with Anti-Diagonal")

choice = int(input("Enter your choice (1–7): "))
n = int(input("Enter the size of the pattern: "))

if choice == 1:
    hollow_square(n)
elif choice == 2:
    square_with_diagonals(n)
elif choice == 3:
    top_bottom_diagonals(n)
elif choice == 4:
    left_right_diagonals(n)
elif choice == 5:
    l_shape_with_diagonal(n)
elif choice == 6:
    reverse_l_with_diagonal(n)
elif choice == 7:
    top_left_with_anti_diagonal(n)
else:
    print("Invalid choice.")
