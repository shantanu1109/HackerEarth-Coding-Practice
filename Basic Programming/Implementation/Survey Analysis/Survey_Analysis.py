import math

# Input: Read responses for each day of the week
responses = []
for _ in range(7):
    response = input()
    responses.append(response)

# Calculate the "Yes" count for each day
yes_counts = [day.count('1') for day in responses]

# Calculate the mean of the "Yes" counts
mean = sum(yes_counts) / len(yes_counts)

# Calculate the squared differences from the mean
squared_diff = [(count - mean) ** 2 for count in yes_counts]

# Calculate the variance (average of squared differences)
variance = sum(squared_diff) / len(yes_counts)

# Calculate the standard deviation (square root of variance)
std_deviation = math.sqrt(variance)

# Output the result rounded to 4 decimal places
print(f"{std_deviation:.4f}")
