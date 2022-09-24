"""
Partial solution to the Covering Points problem.
https://www.hackerrank.com/contests/2022-annual-programming-competition-division-b/challenges/covering-points/

Failed test cases 0 and 9 with wrong answer.
Scored 8 out of 10 points.

Was unsure how to solve the largest test cases without timing out.
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
#  2. INTEGER K
#  3. INTEGER_ARRAY A
#

def solve(N, K, A):
    if (N == K):
        # Number of lines is equal to number of points to be covered.
        return 0
    elif (K == 1):
        # Can only draw one line.
        return (max(A) - min(A))
    else:
        # Remove duplicate coordinates.
        A = sorted(A)
        A = set(A)
        A = list(A)

        # Return (max - min - number_of_gaps).
        return (max(A) - min(A) - (K - 1))
        

if __name__ == '__main__':

    #
    # *********************************************************************
    # *                                                                   *
    # *   Everything from here handles input/output, and may be ignored.  *
    # *                                                                   *
    # *********************************************************************
    #

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    K = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = solve(N, K, A)

    print(result)
