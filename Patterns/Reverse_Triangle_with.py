n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        if j%2==0:
            print(chr(96+j), end=" ")  # Lowercase
        else:
            print(chr(64+j), end=" ")  # Uppercase
    print()
