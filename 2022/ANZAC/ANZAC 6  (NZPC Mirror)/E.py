"""
Solution to Problem E (Children) from 2022 New Zealand Programming Contest 
(ANZAC 6).

Problem was worth 10 points.

Took 2 tries to get it correct because I was missing a full stop on each line
of output on the first try - READ THE OUTPUT FORMAT CAREFULLY!
"""



import pprint # Used only to help with debugging.



# Read number of children.
children = int(input())

# Some variables.
first = ""
second = ""
third = ""

leaderboard = {}

# Read names and zero initialise their scores.
for i in range(children):
    name = input().strip()
    leaderboard[name] = 0

# Read event count and update scores for each child based on the event.
events = int(input())
for i in range(events):
    line = input().split()
    cname = line[0]
    task = line[1]

    if (task == "F" or task == "S"):
        leaderboard[cname] += 20
    
    elif (task == "T" or task == "L"):
        leaderboard[cname] += 25
    
    elif (task == "W"):
        leaderboard[cname] += 15
    
    elif (task == "H"):
        leaderboard[cname] += 30


# Find the chlid with maximum score, save the child's name, and then set the
# child's score to -1.
max_score = 0

for child in leaderboard:
    if (leaderboard[child] > max_score):
        max_score = leaderboard[child]

for child in leaderboard:
    if (leaderboard[child] == max_score):
        leaderboard[child] = -1
        first = child


# Repeat the above to get the child in second place.
max_score = 0

for child in leaderboard:
    if (leaderboard[child] > max_score):
        max_score = leaderboard[child]

for child in leaderboard:
    if (leaderboard[child] == max_score):
        leaderboard[child] = -1
        second = child


# Repeat once more to get the child in third place.
max_score = 0

for child in leaderboard:
    if (leaderboard[child] > max_score):
        max_score = leaderboard[child]

for child in leaderboard:
    if (leaderboard[child] == max_score):
        leaderboard[child] = -1
        third = child


# Print the result.
print(f"Star of the week is {first}.")
print(f"Music CD for {second}.")
print(f"Karakia leader is {third}.")
