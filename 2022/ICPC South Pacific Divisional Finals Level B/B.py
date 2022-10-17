"""
Solution to Problem B (Begrudging Friendship) from ICPC 2022 South Pacific
Divisional Finals (Level B).

This was solved and implemented by my teammates, with a little help from me to
fix wrong answers from the case where there were 3 drinks.
"""



num = int(input()) # Number of drinks.
lststr = input()   # Values of each drink.

ls = lststr.split(" ")
ls = [int(x) for x in ls]
ls.sort()


if num > 3:
    # Second most expensive minus second least expensive.
    print(str(ls[num -2] - ls[1]))
elif num == 2:
    # Least expensive minus most expensive.
    print(str(ls[0] - ls[1]))
elif num == 3:
    # A bit trickier. Two options, take the one that maximises pettiness.
    print(str(max(ls[1] - ls[2], ls[0] - ls[1])))
