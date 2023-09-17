# Read an integer 'n' from the user.
n = int(input())

# Read a string 's' from the user.
s = input()

# Initialize an empty list to store the lengths of consecutive 'H's sequences.
consecutive_house = []

# Initialize a variable 'temp' to keep track of the current consecutive 'H' count.
temp = 0

# Initialize a list 'arr' of length 'n' with empty strings.
arr = [''] * n

# Iterate over each character (j) and its index (i) in the input string 's'.
for i, j in enumerate(s):
    if j == 'H':
        # If the character is 'H', set the corresponding element in 'arr' to 'H',
        # and increment the 'temp' counter.
        arr[i] = 'H'
        temp += 1 
        # If we reach the end of the input string, add the 'temp' count to 'consecutive_house'.
        if i == n - 1:
            consecutive_house.append(temp)
    else:
        # If the character is 'B', set the corresponding element in 'arr' to 'B'.
        arr[i] = 'B'
        # If there were consecutive 'H's before, add the 'temp' count to 'consecutive_house',
        # and reset 'temp' to 0.
        if temp > 0:
            consecutive_house.append(temp)
            temp = 0

# Check if there are no consecutive 'H's or the maximum consecutive 'H' sequence length is 1.
if len(consecutive_house) == 0 or max(consecutive_house) == 1:
    # If the conditions are met, print 'YES' and the resulting arrangement of 'H' and 'B' in 'arr'.
    print('YES')
    print(''.join(arr))
else:
    # Otherwise, print 'NO' to indicate that it's not possible to arrange them as required.
    print('NO')
