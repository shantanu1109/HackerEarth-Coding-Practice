# Function to flip a number
def flip_number(num):
    # Convert the number to a string, reverse it, and then convert it back to an integer
    return int(str(num)[::-1])

# Function to perform the encoding
def encode_and_sum(num1, num2):
    # Flip the two input numbers
    flipped_num1 = flip_number(num1)
    flipped_num2 = flip_number(num2)
    
    # Calculate the sum of the flipped numbers
    encoded_sum = flipped_num1 + flipped_num2
    
    # Flip the result to get the encoded sum
    return flip_number(encoded_sum)

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the two flipped numbers from input
    num1, num2 = map(int, input().split())
    
    # Get the encoded sum for the two flipped numbers
    encoded_sum = encode_and_sum(num1, num2)
    
    # Print the encoded sum for the current test case
    print(encoded_sum)
