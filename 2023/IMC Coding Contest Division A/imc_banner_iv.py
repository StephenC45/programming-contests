"""
'Full' solution to the IMC Banner IV problem from the 2023 IMC x CSESoc x CPMSoc 
Coding Competition Advanced Division.

This solution was written by my teammate.

This sub-optimal solution has a worst-case time complexity of O(n^2) which would 
have timed out if the problem setters wrote good test cases.

The approach is still correct: focus on the M's. Even if this solution did time 
out, we most likely would have reached the optimal solution of prefix summing 
the count of I and C characters eventually.
"""



numChar = int(input())
longString = input()

counterM = 0
counterI = 0
counterC = 0
total = 0

while (counterM < numChar):
    if (longString[counterM] == "M"):
        numOfI = longString[:counterM].count("I")
        numOfC = longString[counterM:].count("C")
        total += (numOfI * numOfC)
    counterM += 1

print(total)
