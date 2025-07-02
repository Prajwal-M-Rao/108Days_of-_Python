print("Enter the filename: ")
fname = input()
fptr = open(fname, 'w')  # 'w' mode creates/truncates the file

for i in range(5):
    print("Enter a name: ")
    data = input()
    fptr.write(data + '\n')

fptr.close()
print("5 names added to file")
