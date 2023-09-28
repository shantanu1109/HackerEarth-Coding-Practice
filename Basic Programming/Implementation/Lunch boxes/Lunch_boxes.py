# Get the number of test cases as input
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the values of n and m for the current test case
    n, m = map(int, input().split())
    
    # Read a list of integers a for the current test case
    a = list(map(int, input().split()))
    
    # Sort the list a in ascending order
    a.sort()
    
    # Initialize variables to keep track of the count and the sum
    count = 0
    su = 0
    
    # Iterate through the sorted list a
    for i in range(len(a)):
        # Check if adding the current element a[i] to the sum su
        # would not exceed the value of n
        if a[i] + su <= n:
            # If it doesn't exceed, add a[i] to su and increment count
            su += a[i]
            count += 1

    # Print the final count for the current test case
    print(count)
