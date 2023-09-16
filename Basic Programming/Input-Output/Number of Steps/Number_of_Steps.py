# Input
n = int(input())  
a = list(map(int, input().split()))  
b = list(map(int, input().split())) 
count = 0  
mi = min(a)  
i = 0  

# Iterate through the arrays to make all elements in 'a' equal
while i < n:
    # Check if the current element in 'a' is greater than or equal to the corresponding element in 'b'
    if a[i] >= b[i]:
        # While the current element in 'a' is greater than the minimum element 'mi', subtract 'b[i]' from 'a[i]'
        while a[i] > mi:
            a[i] -= b[i]
            count += 1  

    # Check if the current element in 'a' becomes less than the minimum element 'mi'
    if a[i] < mi:
        mi = a[i]  
        i = 0  

    # Check if the current element in 'a' is not equal to 'mi'
    if a[i] != mi:
        count = -1  
        break  

    i += 1  # Move to the next element in the arrays

# Print the minimum number of steps required to make all elements in 'a' equal
print(count)
