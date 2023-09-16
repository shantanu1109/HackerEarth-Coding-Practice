# Read the number of test cases (t) from the user
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the values of n and m from the user
    n, m = map(int, input().strip().split())
    
    # Initialize a variable 'ans' to keep track of the maximum count of '#' characters
    ans = 0

    # Loop through each row (n rows) of the grid
    for _ in range(n):
        # Read a row of 'm' characters representing the cells
        cells = input().strip()
        
        # Count the number of '#' characters in the current row and update 'ans' if it's greater
        ans = max(ans, cells.count('#'))
    
    # Print the maximum count of '#' characters in this test case
    print(ans)  
