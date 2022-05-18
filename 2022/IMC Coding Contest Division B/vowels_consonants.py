"""
Full solution to the Vowels and Consonants problem from the 2022 IMC x CSESoc x 
CPMSoc Coding Contest Division B.

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
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER N
#  2. STRING S
#

def solve(N, S):
    # Write your code here
    vowel = ['A','E','I','O','U']
    v = 0
    c = 0
    
    for i in S:
        if i in vowel:
            v += 1
        else:
            c += 1
    if v > c:
        return "VOWELS"
    elif c > v:
        return "CONSONANTS"
    else:
        return "EQUAL"

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

    fptr.write(result + '\n')

    fptr.close()
