"""
Partially correct solution to the Cake Transportation problem from the 2022 IMC 
x CSESoc x CPMSoc Coding Contest Division B.

Failed 1 test case (number 5) out of 9 total test cases with wrong answer.

Total score for this submission: 8.57 out of 10 points.
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
#  2. INTEGER M
#  3. INTEGER_ARRAY x_cake1
#  4. INTEGER_ARRAY y_cake1
#  5. INTEGER_ARRAY x_cake2
#  6. INTEGER_ARRAY y_cake2
#

def solve(N, M, x_cake1, y_cake1, x_cake2, y_cake2):
    cake1_min_x = min(x_cake1)
    cake1_max_x = max(x_cake1)
    
    cake2_min_x = min(x_cake2)
    cake2_max_x = max(x_cake2)
    
    if (cake1_max_x >= cake2_min_x or cake1_min_x >= cake2_max_x):
        return "Collision!"
    else:
        return "No Collision!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #
    # *********************************************************************
    # *                                                                   *
    # *   Everything from here handles input/output, and may be ignored.  *
    # *                                                                   *
    # *********************************************************************
    #

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    M = int(first_multiple_input[1])

    x_cake1 = list(map(int, input().rstrip().split()))

    y_cake1 = list(map(int, input().rstrip().split()))

    x_cake2 = list(map(int, input().rstrip().split()))

    y_cake2 = list(map(int, input().rstrip().split()))

    result = solve(N, M, x_cake1, y_cake1, x_cake2, y_cake2)

    fptr.write(result + '\n')

    fptr.close()
