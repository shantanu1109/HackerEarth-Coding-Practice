# Input: Read the input string
s = input()

# Initialize variables to keep track of the current and maximum lengths
current_length = 1
max_length = 1

# Iterate through the string, starting from the second character (index 1)
for i in range(1, len(s)):
    # Check if the current character is different from the previous character
    if s[i] != s[i - 1]:
        # If they are different, increment the current length
        current_length += 1
    else:
        # If they are the same, update the maximum length if needed
        max_length = max(max_length, current_length)
        current_length = 1

# Update the maximum length one more time to handle the end of the string
max_length = max(max_length, current_length)

# Output: Print the size of the longest good substring
print(max_length)
