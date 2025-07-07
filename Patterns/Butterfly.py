n=int(input("Enter a number: "))
noc=1
nor=(2*n)-1
for i in range(1,2*n):
    for j in range(1,2*n):
        if j <= noc or j >= nor:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    if i < n:
        noc += 1
        nor -= 1
    else:
        noc -= 1
        nor += 1
