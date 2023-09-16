# Input the number of songs
N = int(input())

# Input the list of singers for each song
singers = list(map(int, input().split()))

# Create Dictionary to count occurance of singers
singers_count = {}

# Iterate through the list of singers and count their occurances
for singer in singers:
    if singer in singers_count:
        singers_count[singer] += 1
    else:
        singers_count[singer] = 1

# Find the maximum count of songs for each singer
max_count = max(singers_count.values())

# Count the number of favourite singers
favourite_singers = sum(1 for count in singers_count.values() if count == max_count)

# Output the result
print(favourite_singers)
