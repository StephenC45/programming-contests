"""
Full solution to the Magic Eraser problem from the 2022 IMC x CSESoc x CPMSoc
Coding Contest Division B.
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
#  1. INTEGER X
#  2. INTEGER Y
#

def solve(X, Y):
    number_subcubes = (X // Y) ** 3
    total_surface_area = number_subcubes * Y * Y * 6
    
    return total_surface_area
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #
    # *********************************************************************
    # *                                                                   *
    # *   Everything from here handles input/output, and may be ignored.  *
    # *                                                                   *
    # *********************************************************************
    #

    X = int(input().strip())

    Y = int(input().strip())

    result = solve(X, Y)

    fptr.write(str(result) + '\n')

    fptr.close()