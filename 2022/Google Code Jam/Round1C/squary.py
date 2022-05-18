"""
Partial solution to the Squary problem from Google Code Jam 2022 Round 1C.

Passed test set 1, failed test set 2 with wrong answer.
Also fails the sample for test set 2.

The ideas used in this solution do not match those in the analysis of the
problem and only seems to work for test set 1 through sheer luck - I couldn't
provide an explanation consistent with line 65 and this failed test set 2,
so the logic is most likely wrong. Read the problem analysis instead.
"""



# Didn't end up using this.
import math

# Read number of test cases.
n_tests = int(input())

# List of strings to print as output.
output = []

# Process each test case.
for i in range(n_tests):
    # Read N and K.
    line1 = input().split()
    n = int(line1[0])
    k = int(line1[1])

    # Read the line of integers.
    line2 = input().split()
    for n, item in enumerate(line2):
        line2[n] = int(item)

    # Calculate sum of list and square it.
    sum = 0
    for item in line2:
        sum += item
    squared_sum = sum * sum

    # Calculate sum of squares in list.
    sum_squares = 0
    for item in line2:
        sum_squares += (item * item)
    
    difference = sum_squares - squared_sum

    # If there is no difference, add zero to keep the list squary.
    if (difference == 0):
        output.append(f"Case #{i + 1}: 0")
    elif (sum == 0):
        # Difference not zero, but sum is zero.
        output.append(f"Case #{i + 1}: IMPOSSIBLE")
    else:
        # Find elements to insert.
        num_inserted = 0
        while (difference != 0 and num_inserted < k):
            if (difference < 0):
                absolute_difference = difference * -1 # This variable is unused.
            else:
                absolute_difference = difference # This variable is unused.
            
            # Very questionable... but it somehow worked in test set 1.
            new_element = (difference // (2 * sum))
            
            # Update the relevant sums of the list and increment number of
            # elements inserted. The element is never actually inserted into the
            # list, just the relevant sums are updated.
            sum += new_element
            sum_squares += (new_element * new_element)
            squared_sum = sum * sum
            difference = sum_squares - squared_sum
            num_inserted += 1

            if (num_inserted == 1):
                # Inserting an element for the first time.
                output.append(f"Case #{i + 1}: {new_element}")
            else:
                # Inserting more elements beyond the first.
                output[i] += f" {new_element}"

            if (num_inserted == k and difference != 0):
                # Reached limit for number of insertions but difference is still
                # not zero.
                output[i] = f"Case #{i + 1}: IMPOSSIBLE"


# Print the results of each test case.
for string in output:
    print(string)
