"""
An attempt at the Colouring problem.
https://www.hackerrank.com/contests/2022-annual-programming-competition-division-b/challenges/colouring

Scored 0.75 points (15 out of 200 vertices coloured).

Reads the previous submission (preferably one that scored > 0) and prints a new
sequence with one or two extra vertices coloured in.

Colours in vertices randomly.

I was thinking about running some sort of depth-first search and alternating
the colours but did not have time to implement during the contest.
"""



import random
import time

# Seed random number generator with current time to get closer to true
# randomness.
random.seed(time.time())

# Number of vertices to be coloured in.
N = 300

# Read a previous submission.
colour_list = input().split()

# Randomly colour in a vertex blue. Indices are not good, as can overwrite the
# '#' character needed at the start and excludes last character.
# for i in range(1):
#     colour_list[random.randint(0, 300)] = "B"

# Randomly colour in a vertex red. Indices are not good, as can overwrite the
# '#' character needed at the start and excludes last character.
for i in range(1):
    colour_list[random.randint(0, 300)] = "R"

# Separate input from output to make it easier to copy and paste output into
# the submission editor.
print()
print()

# Print the output.
for i in range(N + 1):
    print(colour_list[i], end=" ")

print()
