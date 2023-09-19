# Prompt the user to input an integer and store it in the variable 'n'
n = int(input())

# Initialize a variable 'answer' to 1, which will be used to calculate the factorial
answer = 1

# Use a for loop to iterate through numbers from 1 to 'n' (inclusive)
for i in range(1, n + 1, 1):
    # Multiply 'answer' by the current value of 'i'
    answer *= i

# Print the final result, which is the factorial of 'n'
print(answer)
