# Input the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input two integers x and k
    x, k = map(int, input().split())
    
    # Initialize a list 'options' with 1 as the first element
    options = [1]
    
    # Initialize 'val' with the value of k
    val = k
    
    # Initialize 'count' to 1
    count = 1
    
    # Build a list of powers of k (k^count) until 'val' exceeds 'x'
    while val <= x:
        count += 1
        options.append(val)
        val = k ** count
        
    # Store the largest power of k in 'total' and remove it from 'options'
    total = options.pop()

    # While 'total' is less than or equal to 'x', try to add elements from 'options' to 'total'
    while total <= x:
        dif = x - total
        # Remove elements from 'options' that are greater than 'dif'
        options = [i for i in options if i <= dif]
        try:
            total += options.pop()
        except:
            break

    # Check if 'total' is equal to 'x' and print "YES" or "NO" accordingly
    if total == x:
        print("YES")
    else:
        print("NO")
