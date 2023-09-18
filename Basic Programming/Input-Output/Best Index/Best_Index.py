import math

# Function to calculate the valid group size for a given number of remaining elements
def get_valid_group_size(remaining_elements):
    # Calculate the group size using the quadratic formula
    factor = (math.sqrt(1 + 8 * remaining_elements) - 1) / 2
    n = int(factor)
    # Return the triangular number associated with the calculated 'n'
    return (n * (n + 1)) // 2

# Taking the number of elements as input
n = int(input())

# Taking a list of integers as input and splitting it
lst = [int(x) for x in input().split()]

xsum, s = [0], 0

# Calculate the prefix sum of the input list 'lst'
for i in lst:
    s += i
    xsum.append(s)

# Initialize 'maximum' with the last element of the input list
maximum = lst[-1]

# Loop through the elements in the input list 'lst'
for i in range(n):
    special_sum = 0
    remaining_elements = n - i

    # Get a valid group size based on the number of remaining elements
    group_size = get_valid_group_size(remaining_elements)

    # Calculate the sum of elements in the valid group
    special_sum = xsum[i + group_size] - xsum[i]

    # Update 'maximum' if the current special_sum is greater
    if special_sum > maximum:
        maximum = special_sum

# Print the maximum special_sum
print(maximum)
