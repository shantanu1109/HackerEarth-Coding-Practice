# Read the number of test cases, T
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input string, S, and the character, k
    S = input()
    k = input()
    
    # Count the occurrences of character k in string S
    out_ = S.count(k)
    
    # Print the count
    print(out_)
