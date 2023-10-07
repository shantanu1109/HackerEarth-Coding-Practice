# Read an integer 'n' from input
n = int(input())

# Loop through 'n' iterations
for _ in range(n):
    # Read two integers 'x' and 'y' from input, separated by a space and assign them to variables
    x, y = map(int, input().split())
    
    # Check conditions for 'x' and 'y'
    if x < 0 or y < 0 or y > x:
        # If any of the conditions is true, print -1
        print(-1)
    else:
        # If all conditions are false, print the maximum of 'x' and 'y'
        print(max(x, y))
