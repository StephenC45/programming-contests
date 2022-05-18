"""
Solution to Problem M (Marvelous Marble Machine) from 2022 ANZAC 1.

Sorts and compares lists.
"""



# Read number of marbles.
n = input()

# Read the lists of marbles.
list1 = input().split(" ") # The input to the machine.
list2 = input().split(" ") # The output from the machine.

if sorted(list1) == sorted(list2):
    print ("marvelous")
else:
    print ("error")