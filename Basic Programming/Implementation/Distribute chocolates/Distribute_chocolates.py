# Read an integer 't' from the user, representing the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read two integers 'c' and 'n' from the user, separated by space
    c, n = map(int, input().split())
    
    # Calculate the minimum number of chocolates required using an arithmetic sum formula
    minimumChocolates = (n * (n + 1)) // 2
    
    # Check if the minimum required chocolates are greater than or equal to 'c'
    if minimumChocolates >= c:
        # If yes, print 'c' because we have enough chocolates
        print(c)
    else:
        # If not, calculate the remaining chocolates needed by subtracting minimumChocolates from 'c'
        c = c - minimumChocolates
        
        # Calculate the remainder when 'c' is divided by 'n', which represents the chocolates distributed among 'n' friends
        ans = c % n
        
        # Print 'ans' as the answer for this test case
        print(ans)
