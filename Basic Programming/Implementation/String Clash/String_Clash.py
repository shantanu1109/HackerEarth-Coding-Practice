# Import the Counter class from the collections module.
from collections import Counter

# Read two lines of input and concatenate them into a single string.
s = input() + input()

# Create a Counter object to count the occurrences of each character in the input string 's'.
char_count = Counter(s)

# Initialize a variable 'total' to keep track of the result.
# This variable will store the total count of characters, with odd-counted characters reduced by 1.
total = sum([i - 1 if (i % 2 == 1) else i for i in char_count.values()])

# Check if 'total' is less than the length of the input string 's'.
# If it is, increment 'total' by 1, else keep it as it is.
result = total + 1 if total < len(s) else total

# Print the final result.
print(result)
