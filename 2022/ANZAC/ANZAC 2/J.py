"""
Solution to Problem J (Social Distancing) from 2022 ANZAC 2.

The table is represented with circular arrays/lists. Be especially careful where
people are seated or being added to the start or end of the table.
"""



def insert_person(index, can_occupied):
    """
    Sets can_occupied[index] and the two adjacent elements to False to indicate
    that a person has been added to the table.
    """
    can_occupied[index] = False

    if (index == 0):
        # Adding person at start of table.
        can_occupied[seat_count - 1] = False
        can_occupied[1] = False
    elif (index == seat_count - 1):
        # Adding person at end of table.
        can_occupied[0] = False
        can_occupied[seat_count - 2] = False
    else:
        # Adding person at neither start nor end of table.
        can_occupied[index - 1] = False
        can_occupied[index + 1] = False

# Read the first line of input.
line1 = input().split()
seat_count = int(line1[0])   # Number of seats at the table.
people_count = int(line1[1]) # Number of people already at table.

# Initlaise table to all false, i.e., all seats initially not occupied.
table = []
for i in range(seat_count):
    table.append(False)

# Read second line of input, store this line in a list.
line2 = input().split()
for item in line2:
    index = int(item)
    table[index - 1] = True # Seat is now occupied.

# A list to indicate if a particular seat can be occupied.
can_occupied = [True for i in range(seat_count)]

# Set values in can_occupied to false according to where everyone is currently
# seated. Does not add any new people.
for index, value in enumerate(table):
    if (value == True):
        can_occupied[index] = False # Cannot occupy where someone is seated.
        
        if (index == 0):
            # Person seated at very start of table.
            can_occupied[seat_count - 1] = False
            can_occupied[1] = False
        elif (index == seat_count - 1):
            # Person seated at very end of table.
            can_occupied[0] = False
            can_occupied[seat_count - 2] = False
        else:
            # Person not at start nor end of table.
            can_occupied[index - 1] = False
            can_occupied[index + 1] = False

# Iterate over table. If there is a seat that can be occupied, add a person.
count = 0
for index, value in enumerate(can_occupied):
    if (value == True):
        insert_person(index, can_occupied)
        count += 1

# Print number of people that can be added to this table without violating
# social distancing requirements.
print(count)
