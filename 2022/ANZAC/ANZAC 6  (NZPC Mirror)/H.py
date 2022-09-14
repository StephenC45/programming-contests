"""
Solution to Problem H (Pointless) from 2022 New Zealand Programming Contest 
(ANZAC 6).

Problem was worth 10 points.
"""

teams = {}
name_list = []

# Read the names of the teams and set their score to zero.
for i in range(4):
    names = input().strip()
    name_list.append(names)
    teams[names] = 0

# Read starting value of jackpot.
jackpot = int(input())

# Read points for first and second round.
line6 = input().split()
line7 = input().split()

# Convert everything in 6th and 7th line of input to int.
for index, item in enumerate(line6):
    line6[index] = int(item)

for index, item in enumerate(line7):
    line7[index] = int(item)

# Add scores to each team.
teams[name_list[0]] += line6[0]
teams[name_list[0]] += line6[7]

teams[name_list[1]] += line6[1]
teams[name_list[1]] += line6[6]

teams[name_list[2]] += line6[2]
teams[name_list[2]] += line6[5]

teams[name_list[3]] += line6[3]
teams[name_list[3]] += line6[4]

# Eliminate team with highest score.
highscore = 0
for pair in teams:
    if (teams[pair] > highscore):
        highscore = teams[pair]

for pair in teams:
    if (teams[pair] == highscore):
        teams[pair] = None
        print(f"Round 1: {pair} are eliminated.")

# Take all remaining teams, reset their score to zero.
round2_teams = {}
name_list = []
for pair in teams:
    if (teams[pair] != None):
        round2_teams[pair] = 0
        name_list.append(pair)

# Add scores to each team.
round2_teams[name_list[0]] += line7[0]
round2_teams[name_list[0]] += line7[5]

round2_teams[name_list[1]] += line7[1]
round2_teams[name_list[1]] += line7[4]

round2_teams[name_list[2]] += line7[2]
round2_teams[name_list[2]] += line7[3]

# Eliminate team with highest score.
highscore = 0
for pair in round2_teams:
    if (round2_teams[pair] > highscore):
        highscore = round2_teams[pair]

for pair in round2_teams:
    if (round2_teams[pair] == highscore):
        round2_teams[pair] = None
        print(f"Round 2: {pair} are eliminated.")

# Add 250 to jackpot on pointless answers (score of 0).
for score in line6:
    if (score == 0):
        jackpot += 250

for score in line7:
    if (score == 0):
        jackpot += 250

# Print value of jackpot.
print(f"Jackpot is GBP{jackpot}.")
