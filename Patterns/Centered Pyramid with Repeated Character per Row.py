n=int(input("Enter a number: "))
noc=1
for i in range(1,n*2):
    for k in range(n-1,noc-1,-1):
        print(" ", end=" ")
    for j in range(1,noc+1):
        print(chr(96+noc), end=" ")
    print()
    if i<n:
        noc += 1
    else:
        noc -= 1
