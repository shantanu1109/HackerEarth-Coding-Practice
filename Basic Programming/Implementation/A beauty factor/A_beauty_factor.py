# Define a function to calculate the beauty factor of a number
def checkBeautyFactor(n):
    su = 0
    
    # Loop through the digits of the number
    for i in str(n):
        su += int(i)
    
    # If the sum has more than one digit, recursively calculate its beauty factor
    if len(str(su)) > 1:
        su = checkBeautyFactor(str(su))
    
    return su

# Read input values for 'b' and 'k' separated by a space
b, k = map(int, input().split())

# Check if k is 9
if k == 9:
    # If k is 9 and b is 9, print a specific number
    if b == 9:
        print(123456789)
    else:
        # If k is 9 but b is not 9, print -1
        print(-1)
else:
    # Initialize a string 'n' with a '1' followed by 'k-1' zeros
    n = "1" + "0" * (k - 1)
    
    # Start an infinite loop
    while True:
        # Check if 'n' contains a '0'; if yes, increment 'n' and continue the loop
        if "0" in str(n):
            n = int(n)
            n += 1
            continue
        
        # Convert 'n' to a string and check if it has duplicate digits
        if len(set(n)) != len(n):
            n = int(n)
            n += 1
            continue
        
        # Calculate the beauty factor of 'n' using the checkBeautyFactor function
        beautyFactor = checkBeautyFactor(str(n))
        
        # If the beauty factor matches 'b', print 'n' and exit the loop
        if beautyFactor == b:
            print(n)
            break
        
        # Increment 'n' and check if it has more than 'k' digits; if yes, print -1 and exit the loop
        n = int(n)
        n += 1
        if len(str(n)) > k:
            print(-1)
            break
