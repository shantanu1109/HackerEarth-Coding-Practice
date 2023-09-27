# Define a function named getRooms that takes three integer parameters: n, m, and k.
def getRooms(n, m, k):
    # Initialize a variable named sum to store the total number of rooms.
    sum = 0

    # Check if n is not divisible evenly by k. If so, set brem to 1; otherwise, set it to 0.
    brem = 1 if n % k != 0 else 0

    # Check if m is not divisible evenly by k. If so, set grem to 1; otherwise, set it to 0.
    grem = 1 if m % k != 0 else 0

    # Calculate the number of rooms by dividing n and m by k, and adding the remainders.
    sum = int(n // k) + int(m // k) + brem + grem

    # Return the total number of rooms.
    return sum

# Read an integer input and store it in the variable tc (test cases).
tc = int(input())

# Iterate through a range of values from 0 to tc-1.
for i in range(tc):
    # Read three space-separated integers (n, m, and k) and store them in variables n, m, and k.
    n, m, k = map(int, input().split())

    # Call the getRooms function with the provided inputs and print the result.
    print(getRooms(n, m, k))
