"""
Solution to Problem F (Flip Flow) from 2022 ANZAC 5.

This code was written by one of my teammates.
"""



line1 = input().split()

line2 = input().split()

line2.append(line1[0])

total = int(line1[1])

previous = int(line2[0])
bot = total

for i in line2[1:]:
    interval = int(i) - previous
    top = bot - interval
    if top < 0:
        top = 0
    bot = total - top
    previous = int(i)

print(top)
