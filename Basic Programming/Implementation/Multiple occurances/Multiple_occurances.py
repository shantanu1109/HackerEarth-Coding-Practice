# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of elements in the array
    n = int(input())

    # Read the elements of the array as a list of integers
    a = list(map(int, input().split()))

    # Create an empty dictionary to store the positions of elements in the array
    d = {}

    # Iterate through the elements of the array
    for i in range(len(a)):
        try:
            # Check if the element already exists in the dictionary
            # If it does, append the current position (i+1) to its list of positions
            if d[a[i]]:
                d[a[i]].append(i+1)
        except:
            # If the element doesn't exist in the dictionary, create a new entry with its position
            d[a[i]] = [i+1]

    # Initialize a variable to store the answer
    ans = 0

    # Iterate through the dictionary items (element, positions list)
    for k, v in d.items():
        # Check if the element appears more than once in the array
        if len(v) >= 2:
            # Add the difference between the last and first positions of the element to the answer
            ans += v[-1] - v[0]

    # Print the answer for the current test case
    print(ans)
