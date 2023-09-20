# Read a string input from the user and store it in the variable input_string.
input_string = input()

# Create a modified string by toggling the case of each character.
modified_string = ''.join(c.lower() if c.isupper() else c.upper() for c in input_string)

# Print the modified string.
print(modified_string)
