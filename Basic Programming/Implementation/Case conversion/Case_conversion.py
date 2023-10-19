# Define a function to convert a camel case string to snake case
def camel_to_snake_case(camel_case_string):
    # Initialize the snake case string with the first character in lowercase
    snake_case_string = camel_case_string[0].lower()
    
    # Iterate through the rest of the characters in the camel case string
    for char in camel_case_string[1:]:
        # Check if the character is an uppercase letter
        if char.isupper():
            # If it's uppercase, add an underscore before it and convert to lowercase
            snake_case_string += '_'
        # Add the character (either uppercase or lowercase) to the snake case string
        snake_case_string += char.lower()
    
    # Return the snake case result
    return snake_case_string

# Input the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the camel case string from the user
    camel_case_string = input()
    
    # Convert the camel case string to snake case using the function
    snake_case_result = camel_to_snake_case(camel_case_string)
    
    # Print the snake case result for this test case
    print(snake_case_result)
