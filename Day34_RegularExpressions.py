#Regular expressions are patterns used to match, search, and replace text.

import re

# Fixed pattern: find emails
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Take user input for the text
text = input("Enter the text to search for emails: ")

# Search for pattern in the text
matches = re.findall(pattern, text)

# Display the result
if matches:
    print(f"\nFound {len(matches)} email(s):")
    for match in matches:
        print(f" - {match}")
else:
    print("\nNo emails found.")
