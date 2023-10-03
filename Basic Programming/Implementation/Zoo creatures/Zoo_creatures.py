# Define a function to find the LCM of two numbers.
def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

# Define a function to find the GCD (Greatest Common Divisor) of two numbers using the Euclidean algorithm.
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Define the main function.
def main():
    # Read an integer 't' from the user, representing the number of test cases.
    t = int(input())
    
    # Iterate through each test case.
    for _ in range(t):
        # Read two integers 'a' and 'b' from the user, separated by a space.
        a, b = map(int, input().split())
        
        # Calculate the LCM of 'a' and 'b' using the find_lcm function.
        lcm_of_hands = find_lcm(a, b)
        
        # Print the results, which are the two fractions: (LCM/a) and (LCM/b).
        print(lcm_of_hands // a, lcm_of_hands // b)

# This block checks if the script is being run directly (not imported as a module).
if __name__ == '__main__':
    main()  # Call the main function if the script is executed directly.
