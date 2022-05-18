"""
Solution to Problem E (Election Paradox) from 2022 ANZAC 2.
"""



# Read the first line of input, containing number of areas.
num_areas = int(input())

# Read populations in each area and sort it in increasing order of size.
votes = input().split()
for i, number in enumerate(votes):
    votes[i] = int(number)

votes.sort()

# Store the maximum number of votes you can get and still lose.
total = 0

# List slicing.
votes1 = votes[:num_areas // 2 + 1]
votes2 = votes[num_areas // 2 + 1:]

for item in votes1:
    total += item // 2

for item in votes2:
    total += item

print(total)
