"""
Partial solution to the Letter Blocks problem from Google Code Jam 2022 Round
1C.

Passed test set 1, failed test set 2 with time limit exceeded.

Uses randomly generated permutations of strings in a brute force approach.
"""



import random

# Read number of test cases.
n_tests = int(input())

# List of strings to print as output.
output = []

def check_string(string):
    """
    Checks if a string would be a valid megatower.

    This validation idea should have been used on individual strings that make 
    up the megatower instead of the megatower itself.
    """
    
    # Get a list of all characters in the string.
    character_list = []
    for character in string:
        if (character not in character_list):
            character_list.append(character)
    
    #print(f"Character list {character_list}")
    
    for char in character_list:
        # Store min and max indices of a particular character.
        min_index = len(string)
        max_index = -1

        for index, letter in enumerate(string):
            if (letter == char and index < min_index):
                min_index = index
            if (letter == char and index > max_index):
                max_index = index
        
        #print(f"Min index of character {char} is {min_index} and max is {max_index}")

        # Check the string to see if there are any different characters between
        # min_index and max_index. If there are different characters, then the
        # string does not adhere to the constraints for a megatower.
        offset = 1
        while (min_index + offset < max_index):
            if (string[min_index + offset] != char):
                return False
            offset += 1
    
    return True



    

for i in range(n_tests):
    # Read two lines, the first containing the number of towers, and the second
    # containing the string for each tower.
    tower_count = int(input())
    tower_list = input().split()

    #print(f"Case {i + 1}: {tower_count} towers, listed below:")
    #print(tower_list)

    # Generate up to 1000 random megatowers. A megatower is a permutation of
    # towers represented as a single string.
    random_count = 0
    while random_count < 1000:
        # Start with empty megatower and track number of added towers and the
        # tower_list indices used in the megatower.
        megatower = ""
        added_towers = 0
        used_indices = [False for i in range(tower_count)]

        # Add towers to megatower until all towers are used.
        while (added_towers < tower_count):
            # Generate random index to get a random tower.
            rand_index = random.randrange(0, tower_count, 1)
            tower = tower_list[rand_index]
            #print(tower)

            # Only add this random tower to the megatower if it has not been
            # used already.
            if (used_indices[rand_index] == False):
                megatower += tower
                used_indices[rand_index] = True
                added_towers += 1

        # The megatower is now built, check if it is valid. If valid, break out
        # of random generation.
        if (check_string(megatower) == True):
            output.append(f"Case #{i + 1}: {megatower}")
            break
        
        random_count += 1
        #print(megatower)
    
    # No valid tower found after generating 1000 random megatowers.
    if (random_count == 1000):
        output.append(f"Case #{i + 1}: IMPOSSIBLE")


# Print the results of each test case.
for string in output:
    print(string)
        