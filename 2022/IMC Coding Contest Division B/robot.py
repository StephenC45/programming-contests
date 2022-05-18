"""
Partially correct solution to the Robot Vacuum problem from the 2022 IMC x 
CSESoc x CPMSoc Coding Contest Division B.

Failed 4 test cases (numbers 3, 4, 5, and 6) out of 7 total test cases with
wrong answer.

Total score for this submission: 3.33 out of 10 points.
"""



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. STRING S
#

def solve(N, S):
    
    u_count = 0
    d_count = 0
    l_count = 0
    r_count = 0
    
    # Count number of up down left right instructions 
    for character in S:
        if (character == "U"):
            u_count += 1
        elif (character == "D"):
            d_count += 1
        elif (character == "L"):
            l_count += 1
        elif (character == "R"):
            r_count += 1
    
    new_string = S
    # Remove instructions so that the robot returns to starting point
    # This means up count == down count, left count == right count.
    while (r_count > l_count):
        new_string = new_string.replace('R', '', 1)
        r_count = r_count - 1
    while (l_count > r_count):
        new_string = new_string.replace('L', '', 1)
        l_count = l_count - 1
    while (u_count > d_count):
        new_string = new_string.replace('U', '', 1)
        u_count = u_count - 1
    while (d_count > u_count):
        new_string = new_string.replace('D', '', 1)
        d_count = d_count - 1
    
    n = len(new_string)
    first_half = ""
    second_half = ""
    
    # The string is now balanced, split into two.
    for i in range(n):
        if (i < math.ceil(n / 2)):
            first_half += new_string[i]
        else:
            second_half += new_string[i]
    
    # First half is outbound trip, second half is inbound trip.
    # Count characters.
    u_count = 0
    d_count = 0
    l_count = 0
    r_count = 0
    
    for character in first_half:
        if (character == "U"):
            u_count += 1
        elif (character == "D"):
            d_count += 1
        elif (character == "L"):
            l_count += 1
        elif (character == "R"):
            r_count += 1
    
    if (u_count > d_count):
        vertical_distance = u_count
    else:
        vertical_distance = d_count
        
    if (l_count > r_count):
        horizontal_distance = l_count
    else:
        horizontal_distance = r_count
    
    return vertical_distance + horizontal_distance
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #
    # *********************************************************************
    # *                                                                   *
    # *   Everything from here handles input/output, and may be ignored.  *
    # *                                                                   *
    # *********************************************************************
    #

    N = int(input().strip())

    S = input()

    result = solve(N, S)

    fptr.write(str(result) + '\n')

    fptr.close()
