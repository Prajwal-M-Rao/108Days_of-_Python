import re

text = "Raavana is the king of Lanka."

# Meta characters used: . (dot) => Matches any single character
regex1 = r"."

# Meta characters used: \. (escaped dot) => Matches literal '.'
regex2 = r"\."

# Meta characters used: | (OR operator) => Matches 'Raavana' or 'Lanka'
regex3 = r"Raavana|Lanka"

text1 = "Ravan is Raavana,not Ravana"

# Meta characters used: + (one or more) => One or more 'R' followed by 'aavana'
regex4 = r'R+aavana'

# Meta characters used: * (zero or more) => Zero or more 'R' followed by 'avana'
regex5 = r'R*avana'

# Meta characters used: ? (zero or one) => Zero or one 'R' followed by 'avana'
regex6 = r'R?avana'

# Meta characters used: ^ (start anchor) => Matches 'Raavana' only if it is at the start of the string
regex7 = r'^Raavana'

# Meta characters used: $ (end anchor) => Matches 'Ravana' only if it is at the end of the string
regex8 = r'Ravana$'

# Perform regex operations
L = re.findall(regex1, text)
M = re.findall(regex2, text)
N = re.findall(regex3, text)
O = re.findall(regex4, text1)
P = re.findall(regex5, text1)
Q = re.findall(regex6, text1)
R = re.findall(regex7, text1)
S = re.findall(regex8, text1)

# Print results
print("Regex1 (match any character '.'): ", L)
print("Regex2 (match literal dot '\\.'): ", M)
print("Regex3 (match 'Raavana' or 'Lanka'): ", N)
print("Regex4 (match 'R+aavana'): ", O)
print("Regex5 (match 'R*avana'): ", P)
print("Regex6 (match 'R?avana'): ", Q)
print("Regex7 (match '^Raavana' at start): ", R)
print("Regex8 (match 'Ravana$' at end): ", S)
