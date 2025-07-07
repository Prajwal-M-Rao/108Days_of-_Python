n=int(input("Enter a number: "))
noc=1
for i in range(1,n*2):
    for j in range(n,noc-1,-1):
        print(chr(96+j), end=" ")
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1
