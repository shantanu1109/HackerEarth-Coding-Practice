# Read three integers 'l', 'r', and 'k' as input, splitting them from a single input line
l, r, k = list(map(int, input().split()))

# Initialize a variable 'count' to 0; it will be used to count the numbers in the range [l, r] that are divisible by 'k'
count = 0

# Use a for loop to iterate through numbers from 'l' to 'r' (inclusive)
for i in range(l, r + 1):
    # Check if 'i' is divisible by 'k' (i.e., 'i' % 'k' equals 0)
    if i % k == 0:
        # If 'i' is divisible by 'k', increment the 'count' variable by 1
        count += 1

# Print the final value of 'count', which represents the count of numbers divisible by 'k' in the range [l, r]
print(count)
