n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%2==0:
            print(chr(64+j), end=" ")  # Uppercase
        else:
            print(chr(96+j), end=" ")  # Lowercase
    print()
