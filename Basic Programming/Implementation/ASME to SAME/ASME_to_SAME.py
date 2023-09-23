# Define the main function
def main():
    # Read the number of test cases, t, from input
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the integer n from input, not used in this code
        n = int(input())
        
        # Read two strings, s and t, from input
        s = input()
        t = input()
        
        # Create a list 'cnt' to store character counts initialized with zeros
        cnt = [0] * 26
        
        # Count the occurrences of characters in string 't'
        for ch in t:
            cnt[ord(ch) - ord('a')] += 1
        
        # Initialize a variable to count wildcards in string 's'
        wildcard = 0
        
        # Iterate through each character in string 's'
        for ch in s:
            if ch == '?':
                # If the character is a '?', increment the wildcard count
                wildcard += 1
            else:
                # If the character is not a '?', decrement the count of that character in 't'
                cnt[ord(ch) - ord('a')] -= 1
        
        # Adjust wildcard count based on character counts in 't'
        for i in range(26):
            wildcard -= max(0, cnt[i])
        
        # Print "Yes" if wildcard count is non-negative, otherwise print "No"
        print("Yes" if wildcard >= 0 else "No")

# Check if the script is run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
