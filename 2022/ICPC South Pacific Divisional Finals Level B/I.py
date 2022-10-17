"""
Solution to Problem I (Incredibly Fun Game) from ICPC 2022 South Pacific
Divisional Finals.
"""



import math


# Read amount of paint you have.
paint = int(input())

# Handle this edge case.
if paint == 2:
    print(1)
    quit()

# Start with (paint - 1) possible ways to paint a two-cell.
answer = paint - 1

# Have a list of factors.
factor_list = []
limit = math.ceil(math.sqrt(paint))

# Populate the list of factors.
for i in range(2, limit + 1):
    if (paint % i == 0):
        factor_list.append(i)
        factor_list.append(paint // i)

# Sort the list and remove duplicates.
factor_list.sort()
factor_list = set(factor_list)
factor_list = list(factor_list)

# For each factor, the height of the two-cell is the factor and the total width
# is (paint // factor). Number of ways to paint a two-cell given this height
# and total width is width - 1.
for factor in factor_list:
    answer += ((paint // factor) - 1)

print(answer)
