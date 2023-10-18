# Function to transform a string to its lexicographically greatest form
def transform_string(s, q):
    vowels = 'aeiou'
    s = list(s)  # Convert the string to a list for easy modification

    for i in range(len(s)):
        if q == 0:
            break
        if s[i] in vowels:
            s[i] = chr(ord(s[i]) + 1)
            q -= 1

    return ''.join(s)

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read input for each test case
    S = input()
    Q = int(input())

    # Transform and print the lexicographically greatest string
    result = transform_string(S, Q)
    print(result)
