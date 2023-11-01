# Function to count the number of ways to select two boxes with a total of K chocolates
def count_ways_to_select_boxes(boxes, K):
    count = 0
    box_counts = {}

    for chocolates in boxes:
        if chocolates in box_counts:
            box_counts[chocolates] += 1
        else:
            box_counts[chocolates] = 1

    for chocolates in boxes:
        complement = K - chocolates

        if complement in box_counts:
            count += box_counts[complement]

        if chocolates * 2 == K:
            count -= 1

    return count // 2

# Input: Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())  # Number of boxes
    chocolates = list(map(int, input().split()))  # Chocolates in each box
    K = int(input())  # Desired total number of chocolates

    ways = count_ways_to_select_boxes(chocolates, K)
    print(ways)
