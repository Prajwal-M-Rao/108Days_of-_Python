# ---------------- Pattern 5: Pyramid ----------------
n=int(input("Enter the value: "))

print("\nPattern 5: Pyramid")
for i in range(1, n + 1):
    for k in range(n, i, -1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*  ", end=" ")
    print()