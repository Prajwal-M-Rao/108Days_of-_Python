# ---------------- Pattern 2: Right-Angled Triangle ----------------
n = int(input("Enter the range: "))
print("\nPattern 2: Right-Angled Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end=" ")
    print()

