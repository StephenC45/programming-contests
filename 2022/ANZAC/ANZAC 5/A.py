"""
Solution to Problem A (Adolescent Architecture) from 2022 ANZAC 5.

This code was written by one of my teammates.
"""



import math

# Read number of blocks used.
block_count = int(input())

# Store cubes and cylinders in separate lists.
cube_list = []
cylinder_list = []

# Read type and size of blocks.
i = 0
while i < block_count:
    newline = input().split()
    temp = newline[1]
    newline[1] = newline[0]
    newline[0] = int(temp)
    if newline[1] == "cube":
        cube_list.append(newline)
    else:
        cylinder_list.append(newline)
    i += 1

# Sort lists in ascending order of size.
cube_list = sorted(cube_list)
cylinder_list = sorted(cylinder_list)


def diffShape(s, r):
    if math.sqrt(2*(r**2)) >= s:
        return 2
    elif s >= (r << 1):
        return 1
    else:
        return 3

# Initialise 2 variables storing the index of the cube and cylinder lists.
last_cu = len(cube_list) - 1
last_cy = len(cylinder_list) - 1

# Start with empty tower and add elements to it. This is done in a similar way
# to mergesort - compare largest cube and largest cylinder, append the "larger"
# of the two, and then print the contents of the tower in reverse order.
tower = []

while last_cu > -1 and last_cy > -1:
    result = diffShape(cube_list[last_cu][0], cylinder_list[last_cy][0])
    if result == 1:
        size = str(cube_list[last_cu][0])
        shape = cube_list[last_cu][1]
        tower.append(shape + ' ' + size)
        last_cu -= 1
    elif result == 2:
        size = str(cylinder_list[last_cy][0])
        shape = cylinder_list[last_cy][1]
        tower.append(shape + ' ' + size)
        last_cy -= 1
    elif result == 3:
        print("impossible")
        quit()

if last_cu == -1:
    while last_cy > -1:
        size = str(cylinder_list[last_cy][0])
        shape = cylinder_list[last_cy][1]
        tower.append(shape + ' ' + size)
        last_cy -= 1
elif last_cy == -1:
    while last_cu > -1:
        size = str(cube_list[last_cu][0])
        shape = cube_list[last_cu][1]
        tower.append(shape + ' ' + size)
        last_cu -= 1

# Print tower in reverse order.
i = len(tower) - 1
while i > -1:
    print(tower[i])
    i -= 1
