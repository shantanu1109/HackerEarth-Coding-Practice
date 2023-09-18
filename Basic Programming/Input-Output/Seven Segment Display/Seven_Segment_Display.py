# Define a dictionary called display_numbers, where keys are digits ('0' to '9')
# and values are the number of matchsticks required to represent each digit.
display_numbers = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

# Read the number of test cases as input.
test_cases = int(input())

# Loop through each test case.
for _ in range(test_cases):
    # Read a string 'n' as input, which represents a number.
    n = input()
    no_of_matchstick = 0

    # Calculate the total number of matchsticks required to represent the input number.
    for i in n:
        no_of_matchstick += display_numbers[i]

    # Case 1: When the total number of matchsticks is even.
    if no_of_matchstick % 2 == 0:
        x = int(no_of_matchstick / 2)
        number = ''
        # Create a number by concatenating '1' x times.
        for i in range(x):
            number = number + '1'
    else:
        # Case 2: When the total number of matchsticks is odd.
        x = int((no_of_matchstick - 3) / 2)
        number = '7'
        # Create a number by concatenating '1' x times after adding '7'.
        for i in range(x):
            number = number + '1'

    # Print the constructed number for this test case.
    print(number)
