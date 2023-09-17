# Read an integer n from the user
n = int(input())

# Read a list of integers a from the user and split them by spaces
a = [int(x) for x in input().split()]

# Check if the last element of the list a is divisible by 10
# If it is, print "Yes"; otherwise, print "No"
print("Yes" if a[-1] % 10 == 0 else "No")
