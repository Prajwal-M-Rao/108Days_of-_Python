# Prompt the user to enter the name of the file where data should be appended
print("Enter the filename: ")
fname = input()  # Takes the filename input from the user

# Open the file in append mode ('a') — this does not erase existing content
fptr = open(fname, 'a')

# Loop to take 5 names as input from the user
for i in range(5):
    print("Enter a name: ")
    data = input()  # Takes a name from the user
    fptr.write(data + '\n')  # Writes the name followed by a newline character to the file

# Close the file after writing is complete
fptr.close()

# Confirmation message
print("5 names added to file")
