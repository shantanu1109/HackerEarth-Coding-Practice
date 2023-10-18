# Read a space-separated line of integers and assign them to the variables P, S, T, H, and x.
P, S, T, H, x = list(map(int, input().split()))

# Initialize a variable 'Sum' to keep track of the sum of values in the loop.
Sum = 0

# Loop 'x' times, where 'x' is a predefined integer.
for i in range(x):
    # Check if the value of 'S' is less than or equal to 'T'.
    if S <= T:
        # If the condition is true, add the value of 'H' to the 'Sum' and decrement 'S' by 1.
        Sum = Sum + H
        S = S - 1
    else:
        # If the condition is false, add the value of 'P' to the 'Sum' and decrement 'S' by 1.
        Sum = Sum + P
        S = S - 1

# After the loop, print the final value of 'Sum'.
print(Sum)
