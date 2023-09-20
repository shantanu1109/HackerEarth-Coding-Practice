# Read the minimum dimension 'l' as input
l = int(input())

# Read the number of test cases 'n' as input
n = int(input())

# Initialize a variable 'i' to 0 to keep track of the current test case
i = 0

# Start a loop that runs for 'n' test cases
while i < n:
    # Read the dimensions 'w' and 'h' as input for the current test case and split them into a list
    wh = input().split()
    w = int(wh[0])  # Width
    h = int(wh[1])  # Height

    # Check if either the width 'w' or the height 'h' is less than 'l'
    if w < l or h < l:
        print('UPLOAD ANOTHER')
    else:
        # Check if both width 'w' and height 'h' are greater than or equal to 'l'
        if w == h and (w >= l and h >= l):
            print('ACCEPTED')
        else:
            print('CROP IT')

    # Increment the test case counter 'i' by 1 to move to the next test case
    i += 1
