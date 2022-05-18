"""
Partial solution to the d1000000 problem from Google Code Jam 2022
Qualification round.

Passed test set 1, failed test set 2 with time limit exceeded.

Uses brute force.
"""



# Read number of test cases.
n_tests = int(input())


die_count_list = []    # List of number of dice for each test case.
list_of_die_lists = [] # List of lists of dice for each test case.


def solve(test_count, die_count_list, list_of_die_lists):
    """
    Given the number of test cases, a list of the number of dice for each test
    case, and a list of lists of dice values for each test case, determines the
    number of dice 
    """
    j = 0
    case_count = 0
    while (j < test_count * 2):
        if (j % 2 == 0):
            if (die_count_list[case_count] < min(list_of_die_lists[case_count])):
                print(f"Case #{case_count + 1}: {die_count_list[case_count]}")
            else:
                die_list = list_of_die_lists[case_count]
                die_list.sort(reverse=True)
                
                len_list = len(die_list)
                index = 0
                straight = []
                max_straight_length = 0

                maximum = max(die_list)
                start_number = maximum
                while (start_number > 0):
                    straight = []
                    straight.append(start_number)

                    index = 1
                    while (index < len_list):
                        if (die_list[index] >= straight[-1] - 1 and start_number - index > 0):
                            straight.append(min(start_number - index, die_list[index]))
                        else:
                            break
                        index += 1

                    if (len(straight) > max_straight_length):
                        max_straight_length = len(straight)
                    
                    start_number -= 1

                print(f"Case #{case_count + 1}: {max_straight_length}")

            case_count += 1

        j += 1

for i in range(n_tests):
    inp = input().split()
    dies = input().split()

    die_count_list.append(int(inp[0]))
    for n, item in enumerate(dies):
        dies[n] = int(dies[n])
    list_of_die_lists.append(dies)

solve(n_tests, die_count_list, list_of_die_lists)