# Function to calculate the cost of the cheapest subarray for a given array
def cheapest_subarray_cost(arr):
    n = len(arr)
    
    if n < 2:
        return -1  # There is no valid subarray
    
    min_cost = float('inf')
    
    for i in range(n - 1):
        cost = arr[i] + arr[i + 1]
        min_cost = min(min_cost, cost)
    
    return min_cost

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the number of elements in the array
    n = int(input())
    
    # Read the array as a list of integers
    arr = list(map(int, input().split()))
    
    # Calculate and print the cost of the cheapest subarray
    result = cheapest_subarray_cost(arr)
    if result == float('inf'):
        print(-1)
    else:
        print(result)
