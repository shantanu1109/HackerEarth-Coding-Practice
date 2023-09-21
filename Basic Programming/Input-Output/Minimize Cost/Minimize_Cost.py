# Define a function 'Solve' that takes two parameters: 'k' (an integer) and 'arr' (a list of integers)
def Solve(k, arr):
    sum1 = 0  # Initialize a variable to store the sum of positive integers
    counter = 0  # Initialize a counter variable to count positive integers encountered
    m = k  # Initialize a variable 'm' to keep track of the remaining positive integers needed
    
    # Iterate through the elements in the 'arr' list
    for i in arr:
        if i >= 0:
            # If the current element is non-negative, increment the counter and add it to the sum
            counter += 1
            sum1 += i
            m = k  # Reset the remaining positive integers needed to 'k'
        else:
            if counter == 0:
                # If no positive integers encountered so far, return the absolute sum of all elements
                return abs(sum(arr) + i)
            else:
                m -= 1  # Decrement the remaining positive integers needed
                if m < 0:
                    # If the required positive integers are already met, add the absolute value of 'i'
                    sum1 += abs(i)
                else:
                    # Otherwise, add the negative integer 'i' to the sum
                    sum1 += i
    
    # Return the absolute sum of positive integers (if any) or the modified sum1
    return abs(sum1)

# Read 'n' (number of elements) and 'k' as input
n, k = map(int, input().split())

# Read the elements of the array 'arr' as input and map them to integers
arr = map(int, input().split())

# Call the 'Solve' function with 'k' and 'arr' as arguments and store the result in 'out_'
out_ = Solve(k, arr)

# Print the final result
print(out_)
