# Import the math module to use mathematical functions
import math

# Get input from the user in the format "hh:mm" and split it into hours (h) and minutes (m)
h, m = map(int, input().split(":"))

# Convert the input time into seconds and store it in the 'temp' variable
temp = h * 60 * 60 + m * 60

# Initialize variables 'a' and 'd'
a = 0
d = 3927.272727272727  # A constant value

# Calculate the result by dividing 'temp' by 'd' and adding 1
ans = temp / d + 1

# Print the floor (integer part) of the result
print(math.floor(ans))
