# Read two integers 'n' and 'k' from user input, where 'n' represents the number of elements and 'k' is a divisor.
n, k = map(int, input().split())

# Initialize a dictionary 'mods' to count the occurrences of remainders when numbers are divided by 'k'.
mods = dict((x, 0) for x in range(k))

# Read a list of integers from user input and process them.
for x in map(int, input().split()):

    # Calculate the remainder of each integer when divided by 'k' and increment its count in the 'mods' dictionary.
    mods[x % k] += 1

# Initialize a variable 'ans' to store the final result.
ans = 0

# Iterate over the keys (remainder values) in the 'mods' dictionary.
for x in mods:

    # Calculate the number of pairs of integers with the same remainder by multiplying the count with itself minus 1,
    # and add it to the 'ans' variable.
    ans += mods[x] * (mods[x] - 1)

# Print the final result, which represents the count of pairs with the same remainder when divided by 'k'.
print(ans)
