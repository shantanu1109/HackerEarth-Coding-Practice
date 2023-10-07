# Read the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the value of n for this test case
    n = int(input())
    total = 0  # Initialize a variable to store the total sum
    
    # Calculate the sum of (n // j) for j in the range from 1 to sqrt(n)
    for j in range(1, int(n**0.5) + 1):
        total += (n // j)
    
    # Double the total and subtract the perfect square value to get the remaining part
    total = 2 * total - int(n**0.5) * int(n**0.5)
    
    # Print the final result for this test case
    print(total)
