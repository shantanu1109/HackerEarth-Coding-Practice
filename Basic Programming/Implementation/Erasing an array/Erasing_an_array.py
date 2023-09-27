# Read the number of test cases from the user
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the length of the array from the user
    n = int(input())
    
    # Read the array elements as a list of integers
    arr = list(map(int, input().split()))
    
    # Initialize a counter variable to 1
    c = 1
    
    # Loop through the elements of the array from the first to the second-to-last element
    for i in range(n-1):
        # Check if the current element is 1 and the next element is 0
        if arr[i] == 1 and arr[i+1] == 0:
            # If the condition is met, increment the counter
            c += 1
    
    # Print the final count for the current test case
    print(c)
