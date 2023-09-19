# Read the input string
s = input()

# Reverse the string and store it in another variable
reversed_s = s[::-1]

# Check if the original string 's' is equal to the reversed string 'reversed_s'
if s == reversed_s:
    print("YES")
else:
    print("NO")
