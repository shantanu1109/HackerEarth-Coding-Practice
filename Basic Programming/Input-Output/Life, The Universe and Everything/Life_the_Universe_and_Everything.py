# Create an infinite loop using 'while True:'
while True:
    # Prompt the user to input an integer and store it in the variable 'n'.
    n = int(input())

    # Check if the value of 'n' is equal to 42.
    if n == 42:
        # If 'n' is 42, exit the loop using 'break'.
        break
    else:
        # If 'n' is not 42, print its value.
        print(n)

# The loop exits when the user inputs 42, and the program continues after the loop.
