# Define a lambda function 'inty' to convert input to an integer
inty = lambda: int(input())

# Define a lambda function 'listy' to convert input to a list of integers
listy = lambda: list(map(int, input().split()))

# Define a lambda function 'mappy' to map input to a list of integers
mappy = lambda: map(int, input().split())

# Import necessary libraries
import math
from collections import defaultdict as dd

# Read the number of test cases (T)
T = inty()

# Loop through each test case
for _ in range(T):
    # Read the integer 'n'
    n = inty()
    
    # Read a list of integers 'alist'
    alist = listy()

    # Initialize 'AND' and 'OR' to -1 and 0 respectively
    AND = -1
    OR = 0

    # Calculate bitwise AND and OR operations for each element in the list
    for i in alist:
        OR |= i  # Bitwise OR operation
        AND &= i  # Bitwise AND operation

    # Convert 'OR' and 'AND' to binary strings, remove '0b' prefix, and count the number of '1's
    OR = bin(OR).replace('0b', '').count('1')
    AND = bin(AND).replace('0b', '').count('1')

    # Calculate the result as 2^(OR - AND)
    res = 1 << (OR - AND)

    # Print the result for this test case
    print(res)
