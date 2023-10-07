# Import the math module to use the math.prod function
import math

# Read an integer 'n' from the user
n = int(input())

# Initialize a variable 'count' to keep track of the count of numbers meeting the criteria
count = 0

# Loop through numbers from 2 to 999999 (inclusive)
for j in range(2, 1000000):
    # Convert the current number 'j' to a string 'i'
    i = str(j)
    
    # Check if 'i' does not contain '1' or '0' and if 'n' is equal to the product of its digits
    if '1' not in i and '0' not in i and (n == math.prod([int(x) for x in i])):
        # If the condition is met, increment the 'count' variable
        count += 1

# Print the final count of numbers that meet the criteria
print(count)
