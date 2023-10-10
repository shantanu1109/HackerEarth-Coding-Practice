# Import the bisect module for efficient binary search and insertion
import bisect  

# Read input
n = int(input())  # Read the number of elements in the bag
bag = []  # Initialize an empty list to represent the bag of numbers
answers = []  # Initialize an empty list to store the answers

# Process each number
for _ in range(n):  # Iterate through each input number
    num = int(input())  # Read the current number
    
    # Use binary search to find the position where 'num' should be inserted in 'bag'
    index = bisect.bisect_left(bag, num)
    
    # Find the smaller and greater elements based on the binary search result
    smaller = bag[index - 1] if index > 0 else -1
    greater = bag[index] if index < len(bag) else -1
    
    # Insert 'num' into the 'bag' while maintaining its sorted order
    bisect.insort_left(bag, num)
    
    # Append the pair of smaller and greater elements to the 'answers' list
    answers.append((smaller, greater))

# Print the answers
for answer in answers:  # Iterate through the list of answers
    print(answer[0], answer[1])  # Print the smaller and greater elements for each input number
