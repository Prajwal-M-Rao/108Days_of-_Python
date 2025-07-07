n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i % 2 != 0:
            print(chr(96+j), end=" ")  # Lowercase
        else:
            print(chr(64+j), end=" ")  # Uppercase
    print()
