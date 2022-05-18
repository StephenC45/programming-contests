"""
Full solution to the IMC Banner III problem from the 2022 IMC x CSESoc x CPMSoc 
Coding Contest Division B.

This code was written by one of my teammates.
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
    # Write your code here
    S = list(S)
    for i in range(len(S)-2):
        print (f"Checking {S[i]} {S[i+1]} {S[i+2]}")
        if (S[i] == 'I' and S[i+1] == 'M' and S[i+2] == '_'):
            S[i+2] = 'C'
        if (S[i] == 'I' and S[i+1] == '_' and S[i+2] == 'C'):
            S[i+1] = 'M'
        if (S[i] == '_' and S[i+1] == 'M' and S[i+2] == 'C'):
            S[i] = 'I'
        if (S[i] == 'I' and S[i+1] == '_' and S[i+2] == '_'):
            S[i+1] = 'M'
            S[i+2] = 'C'
        if (S[i] == '_' and S[i+1] == 'M' and S[i+2] == '_'):
            S[i] = 'I'
            S[i+2] = 'C'
        if (S[i] == '_' and S[i+1] == '_' and S[i+2] == 'C'):
            S[i] = 'I'
            S[i+1] = 'M'
        if (S[i] == '_' and S[i+1] == '_' and S[i+2] == '_'):
            S[i] = 'I'
            S[i+1] = 'M'
            S[i+2] = 'C'    
    return (''.join(S).count("IMC"))

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
