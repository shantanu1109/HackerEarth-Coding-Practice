# Prompt the user to input a string and store it in the variable 'tag'
tag = input()

# Define a list 'li' containing vowels
li = ['A', 'E', 'I', 'O', 'U', 'Y']

# Extract and sum specific digits from the input string 'tag'
chk1 = int(tag[0]) + int(tag[1])
chk2 = int(tag[3]) + int(tag[4])
chk3 = int(tag[4]) + int(tag[5])
chk4 = int(tag[7]) + int(tag[8])

# Check if the third character of 'tag' is a vowel (present in the 'li' list)
if tag[2] in li:
    print('invalid')
# Check if the sums 'chk1', 'chk2', 'chk3', and 'chk4' are all even numbers
elif chk1 % 2 == 0 and chk2 % 2 == 0 and chk3 % 2 == 0 and chk4 % 2 == 0:
    print('valid')
# If none of the above conditions are met, print 'invalid'
else:
    print('invalid')
