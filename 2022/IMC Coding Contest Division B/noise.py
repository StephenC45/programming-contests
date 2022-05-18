"""
Full solution to the Noise Pollution problem from the 2022 IMC x CSESoc x CPMSoc
Coding Contest Division B.

This code was written by one of my teammates.
"""



#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
    
    sports = []
    sports_stats = []
    

    for N_itr in range(N):
        # Process each person in this loop

        first_multiple_input = input().rstrip().split()

        person = first_multiple_input[0]

        loudness = int(first_multiple_input[1])

        numSports = int(first_multiple_input[2])

        for numSports_itr in range(numSports):
            # Process each sport for this person in this loop

            sport = input()
            if not any(d['sport'] == sport for d in sports):
                temp_dict = {
                    "sport" : sport,
                    "person" : person,
                    "loudness" : loudness
                }
                sports.append(temp_dict)
            temp_dict = next(item for item in sports if item["sport"] == sport)
            if (temp_dict["loudness"] < loudness):
                temp_dict["loudness"] = loudness
                temp_dict["person"] = person
            
    for i in sports:
        print (f'In {i["sport"]}, {i["person"]} is the loudest!')

    # Write any more code required and output your answer here
    
    
    
    
    #
    # ***********************************************
    # *                                             *
    # *   This challenge has no `solve` function.   *
    # *   Instead, use the stub code above.         *
    # *                                             *
    # ***********************************************
    #
