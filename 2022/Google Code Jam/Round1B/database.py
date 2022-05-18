"""
Partial solution to the ASeDatAb problem from Google Code Jam 2022 Round 1B.

Passed test set 1, failed test set 2 with wrong answer.

The most important idea is that for any number n, using n XOR n (using the 
bitwise XOR operator on itself) will always produce zero.

You must download the local testing tool and interactive runner, then use the
following command:
python interactive_runner.py python3 local_testing_tool.py 0 -- python3 database.py
"""



import random
import sys

# Read number of test cases.
n_tests = int(input())

"""
Generates a random binary string with num_of_ones bits being 1, and the
rest being zero.
"""
def generate_binary_string(num_of_ones):
    # Start with empty string.
    string = ""

    if (num_of_ones > 4):
        count = 8 - num_of_ones
    else:
        count = num_of_ones
    
    # Using count variable slightly improves the efficiency of this function.
    # This prevents having to generate 8 unique random indices.
    random_index_list = []
    i = 0
    while (i < count):
        # Generate random index.
        rand_index = random.randrange(0, 8, 1)
        #print(rand_index)

        # Only append and increment i if not already in list.
        if (rand_index not in random_index_list):
            i += 1
            random_index_list.append(rand_index)
        #print(random_index_list)

    # Generate the string.
    index = 0
    while (index < 8):
        if (index in random_index_list and count == num_of_ones):
            string += "1"
        elif (index in random_index_list and count != num_of_ones):
            string += "0"
        elif (count == num_of_ones):
            string += "0"
        elif (count != num_of_ones):
            string += "1"
        index += 1

    return string
    

# Generate an initial random binary string with 4 zeros to give to judge for
# first test case.
string = generate_binary_string(4)
print(string)
sys.stdout.flush()

# Process i test cases.
i = 0
while (i < n_tests):
    # Read judge output, which contains number of ones.
    number_of_ones = int(input())

    # Test case failed. Terminate program.
    if (number_of_ones == -1):
        quit()

    # Test case passed. Increment i.
    elif (number_of_ones == 0):
        i += 1
        if (i < n_tests):
            # Only generate new string if not all tests finished.
            string = generate_binary_string(4)
            print(string)
            sys.stdout.flush()

    # Test case not passed, but not failed.
    else:
        # Make new binary string where number of 1 bits is same as judge output.
        # If this new string is the same as the hidden value stored in the
        # record and the judge chooses r = 0, then the record will be set to
        # 00000000.
        string = generate_binary_string(number_of_ones)
        print(string)
        sys.stdout.flush()
