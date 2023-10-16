# Read the input string containing the sequence of dice rolls
str = input()

# Initialize variables to count the number of girls (c) and a flag for invalid sequences (flag)
c = 0
flag = False

# Iterate through each character in the input string
for char in str:
    # Check if the character is greater than '6'
    if char > '6':
        flag = True  # Set the flag to indicate an invalid sequence
        break
    # If the character is '6', continue to the next character
    elif char == '6':
        continue
    c += 1  # Increment the count for each character that's not '6'

# Check if the flag is set (indicating an invalid sequence) or the last character is '6
if flag or str[-1] == '6':
    print("-1")  # Print -1 for an invalid sequence
else:
    print(c)  # Print the number of girls if the sequence is valid
