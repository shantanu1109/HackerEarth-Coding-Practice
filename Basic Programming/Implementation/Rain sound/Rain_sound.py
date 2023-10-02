# Read an integer 't' from the user, representing the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read three integers 'l', 'r', and 's' from the user, representing the input values for the current test case
    l, r, s = map(int, input().split())
    
    # Check if 's' is greater than 'r'
    if s > r:
        # If 's' is greater than 'r', it's impossible to find a valid range, so print (-1, -1)
        print(-1, -1)
    else:
        # Calculate the minimum possible integer 'mi' such that (mi * s) is greater than or equal to 'l'
        mi = int(((l - 1) / s) + 1)
        
        # Calculate the maximum possible integer 'ma' such that (ma * s) is less than or equal to 'r'
        ma = r // s
        
        # Check if 'mi' is greater than 'ma', indicating that there is no valid range
        if mi > ma:
            # If 'mi' is greater than 'ma', it's impossible to find a valid range, so print (-1, -1)
            print(-1, -1)
        else:
            # Print the calculated 'mi' and 'ma' as the valid range for this test case
            print(mi, ma)
