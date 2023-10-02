# Read an integer 't' from the user, representing the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read an integer 'n' from the user
    n = int(input())
    
    # Initialize 'ans' to 1
    ans = 1
    
    # Calculate 'ans' by adding (n-1)*n to it
    ans += (n - 1) * n
    
    # Print the value of 'ans' for the current test case
    print(ans)
