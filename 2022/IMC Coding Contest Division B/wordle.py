"""
Full solution to the Wordle problem from the 2022 IMC x CSESoc x CPMSoc Coding 
Contest Division B.

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
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. STRING_ARRAY allowed_words
#  3. INTEGER K
#  4. STRING_ARRAY guesses
#  5. STRING_ARRAY responses
#


def check(guess, ans):
    t = ''
    for i in range(len(guess)):
        if guess[i] == ans[i]:
            t += 'G'
        elif guess[i] in ans:
            t += 'Y'
        else:
            t += '.'
    return t

def copy(real):
    temp = []
    for i in real:
        temp.append(i)
    return temp

def solve(N, allowed_words, K, guesses, responses):
    # Write your code here
    temp = copy(allowed_words)
    for i in range(len(guesses)):
        for j in allowed_words:
            if (check(guesses[i],j) != responses[i]):
                temp.remove(j)
        allowed_words = copy(temp)
    return temp
    
    

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

    allowed_words = []

    for _ in range(N):
        allowed_words_item = input()
        allowed_words.append(allowed_words_item)

    K = int(input().strip())

    guesses = []

    for _ in range(K):
        guesses_item = input()
        guesses.append(guesses_item)

    responses = []

    for _ in range(K):
        responses_item = input()
        responses.append(responses_item)

    result = solve(N, allowed_words, K, guesses, responses)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
