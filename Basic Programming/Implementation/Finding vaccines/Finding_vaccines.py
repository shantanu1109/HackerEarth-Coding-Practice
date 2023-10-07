# Import the Counter class from the collections module
from collections import Counter

# Read the number of vaccines
n = int(input())

# Read the length of the RNA string
m = int(input())

# Read the RNA string
rna = input()

# Create a Counter object to count the occurrences of each character in the RNA string
rna_counter = dict(Counter(rna))

# Define constants for the nucleotides
guanine = 'G'
cytosine = 'C'

# Initialize variables to keep track of the best vaccine and its number
best = 0
vaccine_number = 0

# Loop through each vaccine
for _ in range(n):
    # Read the length of the vaccine's sequence
    l = int(input())
    
    # Read the vaccine's sequence
    s = input()
    
    # Create a Counter object to count the occurrences of each character in the vaccine's sequence
    s_counter = dict(Counter(s))
    
    # Calculate the "status" of the vaccine, which is the product of G-C and C-G pairs
    status = s_counter.get(cytosine, 0) * rna_counter.get(guanine, 0) + s_counter.get(guanine, 0) * rna_counter.get(cytosine, 0)
    
    # If the current vaccine has a higher status than the best one found so far, update the best and its number
    if status > best:
        best = status
        vaccine_number = _ + 1

# Print the number of the best vaccine
print(vaccine_number)
