# Read the dimensions of the matrix 'n' and 'm'
n, m = map(int, input().split())

# Initialize variables to store maximum values and the rook's position
maxi = 0
x = 0
y = 0

# Create an empty matrix 'a' to store the values
a = []

# Read the matrix values and store them in the 'a' matrix
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# Initialize lists to store row sums and column sums
row_sums = [0] * n
col_sums = [0] * m

# Calculate row sums and column sums
for i in range(n):
    for j in range(m):
        row_sums[i] += a[i][j]
        col_sums[j] += a[i][j]

# Find the position to place the rook such that the sum of cells under attack is maximized
for i in range(n):
    for j in range(m):
        if row_sums[i] + col_sums[j] - 2 * a[i][j] > maxi:
            x = i
            y = j
            maxi = row_sums[i] + col_sums[j] - 2 * a[i][j]

# Print the position of the rook (adding 1 to the row and column indices to match 1-based indexing)
print(x + 1, y + 1)
