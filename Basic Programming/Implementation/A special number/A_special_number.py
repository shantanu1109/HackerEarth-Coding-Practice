# Define a function named getSum that takes an integer n as input.
def getSum(n):
    su = 0  # Initialize a variable su to store the sum of digits, starting at 0.
    
    # Create a while loop to iterate until n becomes 0.
    while n != 0:
        rem = n % 10  # Get the rightmost digit of n.
        su += rem    # Add the rightmost digit to su.
        n = n // 10  # Remove the rightmost digit from n.
    
    return su  # Return the sum of digits.

# Read an integer n from the user.
n = int(input())

# Initialize an empty list named li.
li = []

# Iterate from 0 to n-1.
for i in range(n):
    # Read an integer x from the user.
    x = int(input())
    
    # Iterate from x to a large number (10,000,000,000 in this case).
    for i in range(x, 10000000000):
        # Call the getSum function to calculate the sum of digits of i.
        su = getSum(i)
        
        # Check if the sum su is divisible by 4.
        if su % 4 == 0:
            # If su is divisible by 4, print i and break out of the loop.
            print(i)
            break
