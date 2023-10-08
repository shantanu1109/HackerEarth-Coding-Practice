# Define a function called "is_inverse" that takes a list of integers called "nums" as input.
def is_inverse(nums):
  # Iterate over the elements in "nums" along with their index using "enumerate".
  for i, num in enumerate(nums):
    # Check if the index incremented by 1 is not equal to the value at index "num - 1".
    # Inverse implies that the value at index i should be (i+1), so we are checking this condition.
    if i + 1 != nums[num - 1]:
      # If the condition is not met, return False, indicating that it is not an inverse.
      return False
  # If the loop completes without returning False, return True, indicating it is an inverse.
  return True

# The following code block runs when the script is executed directly (not imported as a module).
if __name__ == "__main__":
  # Read an integer "t" from the user as the number of test cases.
  t = int(input())
  
  # Iterate through each test case.
  for _ in range(t):
    # Read an integer "n" from the user as the length of the list.
    n = int(input())
    
    # Read a list of integers from the user, splitting the input and converting it to a list of integers.
    nums = list(map(int, input().split()))
    
    # Call the "is_inverse" function with the input list "nums" and check if it's an inverse.
    if is_inverse(nums):
      # If it's an inverse, print "inverse".
      print("inverse")
    else:
      # If it's not an inverse, print "not inverse".
      print("not inverse")
