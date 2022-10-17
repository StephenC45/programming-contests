"""
Solution to Problem D (Dig and Drill) from ICPC 2022 South Pacific Divisional 
Finals (Level B).
"""



x = int(input())

count = 0
while(x != 0):
    dig = x % 3
    if dig == 0:
        x = x//3
        count += 1
    else:
        count += dig
        x -= dig

print(count)
