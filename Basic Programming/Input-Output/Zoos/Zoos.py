# Read input word
word = input().upper()

# Count the number of 'Z's and 'O's
count_z = word.count('Z')
count_o = word.count('O')

# Check if it's similar to 'zoo'
if count_z * 2 == count_o:
    print("Yes")
else:
    print("No")
