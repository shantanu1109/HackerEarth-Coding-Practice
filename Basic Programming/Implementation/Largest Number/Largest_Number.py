# Read input values n and k
n, k = map(int, input().split())

# Convert n to a string and store its digits in a list
n_str = str(n)
digits = [int(digit) for digit in n_str]

# Define a function to find the largest number by removing k digits
def find_largest_number(digits, k):
    stack = []
    for digit in digits:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If k is still greater than 0, remove the remaining k digits from the end
    while k > 0:
        stack.pop()
        k -= 1
    
    # Convert the stack to a string and join the digits to form the largest number
    largest_number = ''.join(map(str, stack))
    
    return largest_number

# Find and print the largest number
result = find_largest_number(digits, k)
print(result)
