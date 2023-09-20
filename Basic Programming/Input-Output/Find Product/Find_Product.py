# Read the size of the array
N = int(input())

# Read the elements of the array as a list of integers
A = map(int, input().split())

# Initialize a variable 'product' to store the product of all elements
product = 1

# Iterate through each element in the array 'A'
for i in A:
    # Calculate the product of 'product' and the current element 'i' modulo (10^9 + 7)
    product = (product * i) % (10**9 + 7)

# Print the final result, which is the product of all elements modulo (10^9 + 7)
print(product)
