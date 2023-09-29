# Prompt the user to enter an integer 't', which represents the number of test cases
t = int(input())

# Loop 't' times to process each test case
for i in range(t):
    # Prompt the user to enter an integer 'n' for each test case
    n = int(input())
    
    # Calculate the result for the current test case
    result = n * (n + 1)
    
    # Print the result for the current test case
    print(result)
