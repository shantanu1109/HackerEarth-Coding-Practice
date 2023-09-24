# Define a function called Minimum_Operations that takes two arguments: n and s
def Minimum_Operations(n, s):
    # Create a set from the string s to remove duplicate characters
    set_s = list(set(s))
    
    # Initialize a variable to keep track of the number of reduce operations
    reduce_op = 0
    
    # Iterate through the unique characters in set_s
    for i in range(len(set_s)):
        # Count the number of occurrences of the current character and divide by 2
        # This represents the number of reduce operations needed for this character
        reduce_op += s.count(set_s[i]) // 2
    
    # Return the total number of reduce operations
    return reduce_op

# Read the number of test cases as input
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the value of n (not used in your function, consider removing it)
    n = int(input())
    
    # Read the string s for the current test case
    s = input()
    
    # Call the Minimum_Operations function with n and s and store the result in out_
    out_ = Minimum_Operations(n, s)
    
    # Print the result for the current test case
    print(out_)
