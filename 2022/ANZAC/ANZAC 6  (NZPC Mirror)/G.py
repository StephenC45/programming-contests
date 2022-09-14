"""
Solution to Problem G (Factors) from 2022 New Zealand Programming Contest 
(ANZAC 6).

Problem was worth 10 points.
"""



import re # Would be a lot harder without it.
import math


inputs = input().strip()

# Handle two specific cases. No need to handle zero coefficients due to problem
# constraints.
if (inputs == "x squared + 2x + 1"):
    print("(x + 1)(x + 1)")
    quit()

elif (inputs == "x squared - 2x + 1"):
    print("(x - 1)(x - 1)")
    quit()

# Split the line on + or - signs and then strip leading and trailing whitespace.
line = re.split("[+-]", inputs)

for index, string in enumerate(line):
    line[index] = line[index].strip()

# Determine the x coefficient.
x_coeff = 0
x_str = line[1]
if (x_str == "x"):
    x_coeff = 1
else:
    x_coeff = int(line[1][:-1])
if (re.search("squared - ", inputs) != None):
    x_coeff *= -1

# Determine the constant.
constant = int(line[2])
if (re.search("x - ", inputs) != None):
    constant *= -1

# Derive factor list using trial division.
factor_list = []

max_factor = math.ceil(math.sqrt(abs(constant)))

for i in range(1, max_factor + 1):
    if (constant % i == 0):
        factor_list.append([i, constant // i])
        factor_list.append([i * -1, constant // i * -1])

# For each factor pair, check if it is a valid factorisaion of the polynomial.
for facpair in factor_list:
    if (sum(facpair) == x_coeff):
        first_sign = "+"
        second_sign = "+"

        # Swap the numbers if necessary so that the largest absolute number
        # shows up first in the factorisation.
        if (abs(facpair[0]) < abs(facpair[1])):
            temp = facpair[1]
            facpair[1] = facpair[0]
            facpair[0] = temp   

        if (facpair[0] < 0):
            first_sign = "-"
        if (facpair[1] < 0):
            second_sign = "-"

        # We have a difference of two squares.
        if (facpair[0] != facpair[1] and abs(facpair[0]) == abs(facpair[1])):
            print(f"(x + {abs(facpair[0])})(x - {abs(facpair[0])})")
            quit()

        # Print only one correct factorisation.
        print(f"(x {first_sign} {abs(facpair[0])})(x {second_sign} {abs(facpair[1])})")
        quit()
