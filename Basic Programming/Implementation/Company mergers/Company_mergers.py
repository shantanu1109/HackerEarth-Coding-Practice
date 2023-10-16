# Import necessary libraries
from collections import Counter
import numpy as np

# Read the number of test cases (n) and the length of the list (m)
n = int(input())
m = int(input())

# Initialize an empty list to store input data
mar = []

# Read and store the input data as lists
for i in range(n):
   mar.append(input().split(' '))

# Convert the list of lists to a numpy array
mar = np.array(mar)

# Flatten the numpy array to a 1D array
mar = mar.flatten()

# Count the occurrences of each element and store them in a dictionary
mar = Counter(mar)

# Convert the dictionary values to a list
mar = list(mar.values())

# Find the maximum count of any element in the list
M = max(mar)

# Check if the maximum count is greater than 2
if M > 2:
   # Count how many elements have the maximum count
   C = mar.count(M)
   # Initialize a count of elements that need to be removed (initialized as max count - 2)
   count = max(mar) - 2

   # Check if there is more than one element with the maximum count and not all elements have the maximum count
   if C > 1 and C != len(mar):
       count += 1
else:
   count = 0  # Set count to 0 if the maximum count is 2 or less

# Print the final count
print(count)
