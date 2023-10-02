# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input string for the current test case
    s = input()
    
    # Check if the string is a palindrome
    if s == s[::-1]:
        print(-1)  # If it's a palindrome, print -1
    else:
        # If it's not a palindrome, sort the characters and print the sorted string
        s = sorted(s)
        print("".join(s))
