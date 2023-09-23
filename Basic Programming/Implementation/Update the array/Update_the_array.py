# Define a function to calculate the minimum updates needed
def min_updates(N, A, K):
    # Check if N is odd, if so, it's not possible to proceed
    if N % 2:
        return -1
    
    # Initialize counters and dictionaries to keep track of odd and even numbers
    count_odd = 0
    count_even = 0
    req_odd = 0
    req_even = 0
    od = {}  # Dictionary to store occurrences of odd numbers
    ev = {}  # Dictionary to store occurrences of even numbers
    
    # Iterate through the list A
    for i in range(N):
        if A[i] % 2 and od.get(A[i], 0) == 0:
            # If the number is odd and hasn't been counted yet, increment count_odd
            count_odd += 1
            # Mark the occurrence of the odd number in the dictionary
            od[A[i]] = 1
            # Check if the odd number is less than or equal to K, and if so, increment req_odd
            if A[i] <= K:
                req_odd += 1
        elif A[i] % 2 == 0 and ev.get(A[i], 0) == 0:
            # If the number is even and hasn't been counted yet, increment count_even
            count_even += 1
            # Mark the occurrence of the even number in the dictionary
            ev[A[i]] = 1
            # Check if the even number is less than or equal to K, and if so, increment req_even
            if A[i] <= K:
                req_even += 1
    
    # Calculate the required counts to balance odd and even numbers
    count_odd = max(0, N // 2 - count_odd)
    count_even = max(0, N // 2 - count_even)
    req_even = K // 2 - req_even
    req_odd = (K - K // 2) - req_odd
    
    # Check if the requirements can be met, if not, return -1
    if req_even < count_even or req_odd < count_odd:
        return -1
    
    # Calculate and return the absolute sum of count_even and count_odd
    return abs(count_even + count_odd)

# Define the main function
def main():
    # Read the number of test cases
    T = int(input())
    assert 1 <= T <= 100
    
    # Loop through each test case
    for _ in range(T):
        # Read the length of the list and the list itself
        N = int(input())
        assert 1 <= N <= 100000
        A = list(map(int, input().split()))
        for i in A:
            assert 1 <= i <= 1000000000
        # Read the value of K
        K = int(input())
        assert 1 <= K <= 1000000000
        
        # Call the min_updates function and print the result
        out = min_updates(N, A, K)
        print(out)

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
