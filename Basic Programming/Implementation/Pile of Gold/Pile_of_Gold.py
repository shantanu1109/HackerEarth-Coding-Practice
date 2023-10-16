# Define the 'solve' function to determine and print the winner based on pile sizes
def solve(pile_1, pile_2):
    # Check if both pile sizes are odd
    if pile_1 % 2 == 1 and pile_2 % 2 == 1:
        print("Jeel")
    else:
        print("Ashish")

# Define the 'main' function to handle test cases
def main():
    # Read the number of test cases
    no_of_test_cases = int(input())

    # Iterate through each test case
    for _ in range(no_of_test_cases):
        # Read the pile sizes for the current test case
        pile_1, pile_2 = map(int, input().split())

        # Call the 'solve' function to determine the winner and print the result
        solve(pile_1, pile_2)

# Ensure that the 'main' function is executed when the script is run
if __name__ == "__main__":
    main()
