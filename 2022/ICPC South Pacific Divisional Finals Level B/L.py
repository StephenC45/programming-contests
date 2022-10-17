"""
Solution to Problem L (Lugging Ladders) from ICPC 2022 South Pacific Divisional 
Finals (Level B).

This was solved and implemented by my teammates.
"""



seq = input().strip()
ls = seq.split()

Ucount = 0
Dcount = 0

threeLoc = "U"
threeE = 0
fourLoc = "D"
fourE = 0

for i in seq:
    next = i
    if next == "U":
        Ucount += 1
        if threeLoc == "D":
            threeLoc = "U"
            threeE += 1
        if  fourLoc == "D":
            fourLoc = "U"
            fourE += 1


    elif next == "D":
        Dcount += 1
        if threeLoc == "U":
            threeLoc = "D"
            threeE += 1
        if  fourLoc == "U":
            fourLoc = "D"
            fourE += 1

print(f"{Dcount*2} {Ucount*2} {threeE} {fourE}")
