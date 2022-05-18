"""
Solution to Problem J (Code Guessing) from 2022 ANZAC 1.

Uses casework to solve the problem in O(1) time.
"""



# Read first line of input, which contain the known cards A1 and A2.
cards = input().split(" ")
A1 = int(cards[0])
A2 = int(cards[1])

# Read the second line of input.
input_str = input()

if (input_str == "AABB"):
    if A2 == 7:
        print("8 9")
    else:
        print("-1")
elif (input_str == "BBAA"):
    if A1 == 3:
        print("1 2")
    else:
        print("-1")
elif (input_str == "ABAB"):
    if A1 == 6 and A2 == 8:
        print("7 9")
    else:
        print("-1")
elif (input_str == "BABA"):
    if A1 == 2 and A2 == 4:
        print("1 3")
    else:
        print("-1")
elif (input_str == "ABBA"):
    if A2 - A1 == 3:
        print(f"{A1 + 1} {A2 - 1}")
    else:
        print("-1")
elif (input_str == "BAAB"):
    if A1 == 2 and A2 == 8:
        print("1 9")
    else:
        print("-1")