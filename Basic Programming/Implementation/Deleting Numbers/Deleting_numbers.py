# Input: Read the values of 'n' and 'k' separated by a space
n, k = map(int, input().split())

# Create a list 'A' to store 'n' values. Initialize with a placeholder at index 0.
A = [0]

# Read 'n' integer values and store them in the 'A' list.
A += list(map(int, input().split()))

# Calculate the middle index of the list 'A'
middle = (n + 1) // 2

# Calculate the value of 'N' based on 'n' and 'k'
N = n - k

# Calculate the middle index for the modified list 'A'
Middle = (N + 1) // 2

# Calculate the ending index for the modified list 'A'
End = Middle + k

# Extract a subarray 'a' from 'A' using slicing
a = A[Middle:End + 1]

# Initialize 'max_value' with the minimum possible integer value
max_value = max(a)  # Find the maximum value in the subarray 'a'

# Output: Print the maximum value found in the subarray
print(max_value)
