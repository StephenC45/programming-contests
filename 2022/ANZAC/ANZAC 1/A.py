"""
Solution to Problem A (Espresso!) from 2022 ANZAC 1.
"""



# Read first line of input.
n = input().split(' ')
water_in_tank = int(n[1])
refill_count = 0

# Store the next lines of input in a list.
input_list = []
for i in range(int(n[0])):
    input_list.append(input())

# Iterate over the list and determine the amount of water needed.
for item in input_list:
    # Determine amount of water needed.
    if 'L' in item:
        water_required = int(item[0]) + 1
    else:
        water_required = int(item[0])
    
    # Refill the tank if necessary before subtracting the water needed.
    if water_required > water_in_tank:
        refill_count += 1
        water_in_tank = int(n[1])

    water_in_tank -= water_required

# Print the number of times the tank was refilled.
print(refill_count)