# Function to calculate the minimum cost for each test case.
def minimum_cost(test_cases):
    for test_case in test_cases:
        green_cost, purple_cost = test_case['costs']
        num_participants = test_case['num_participants']
        participants = test_case['participants']
        
        cost_if_green = sum([p[0] for p in participants])
        cost_if_purple = sum([p[1] for p in participants])
        
        # Choose the minimum cost between using green for problem 1 and purple for problem 2,
        # and using purple for problem 1 and green for problem 2.
        min_cost = min(green_cost * cost_if_green + purple_cost * cost_if_purple,
                       purple_cost * cost_if_green + green_cost * cost_if_purple)
        
        print(min_cost)

# Input parsing
num_test_cases = int(input())
test_cases = []

for _ in range(num_test_cases):
    costs = list(map(int, input().split()))
    num_participants = int(input())
    participants = []
    for _ in range(num_participants):
        participants.append(list(map(int, input().split())))
    
    test_case = {
        'costs': costs,
        'num_participants': num_participants,
        'participants': participants
    }
    test_cases.append(test_case)

# Calculate and print minimum costs
minimum_cost(test_cases)
