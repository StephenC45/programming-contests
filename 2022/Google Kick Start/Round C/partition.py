"""
Partially correct solution to the Range Partition problem from Google Kick Start
2022 Round C.

Passed test set 1, failed test set 2 with wrong answer.

This solution is efficient enough, but the method used was wrong. The method
used here was to attempt to remove elements from the set containing Alan's
numbers.

What I should have done was to partition into an entirely new set. I also didn't
realise that there is only a possible solution if the total sum of the numbers
from 1 to N inclusive is divisible by (X + Y) so that may have caused wrong
answers for if the test case was POSSIBLE or IMPOSSIBLE.
"""



# Read the number of test cases.
test_count = int(input())

# Process each test case.
curr_test = 1
while (curr_test <= test_count):
    line = input().split()
    N = int(line[0])
    X = int(line[1])
    Y = int(line[2])

    # Find the target for Alan.
    total_sum = (N * (N + 1)) // 2
    total_ratio = X + Y
    target_alan = (total_sum * (X / total_ratio))

    difference = total_sum - target_alan
    
    # Initially, I had Alan start with all the numbers. It would have been
    # easier to start with an empty set for Alan (i.e., alan_sum = 0 and
    # alan_list = []).
    max_alan = N
    alan_sum = total_sum
    barbara_sum = 0
    alan_list = [(i + 1) for i in range(N)]

    # Greedily remove the largest possible element from Alan's list until the
    # sum of Alan's list matches Alan's target.
    alan_count = N
    while (difference != 0 and alan_count > 0):
        difference_copy = difference
        if (difference <= max_alan):
            alan_sum -= alan_list[int(difference) - 1]
            barbara_sum += alan_list[int(difference) - 1]
            alan_list[int(difference) - 1] = 0
            difference -= difference_copy

        else:
            alan_sum -= alan_list[max_alan - 1]
            barbara_sum += alan_list[max_alan - 1]
            difference -= alan_list[max_alan - 1]
            alan_list[max_alan - 1] = 0
            max_alan -= 1
        
        if (difference != difference_copy):
            alan_count -= 1
    
    # This should have been checked much earlier using
    # if (total_sum % (X + Y) != 0):
    if (alan_sum / barbara_sum != X / Y):
        print(f"Case #{curr_test}: IMPOSSIBLE")
        curr_test += 1
        continue

    print(f"Case #{curr_test}: POSSIBLE")
    print(alan_count)
    for item in alan_list:
        if (item > 0):
            print(item, end=' ')
    print(end='\n')
    
    curr_test += 1