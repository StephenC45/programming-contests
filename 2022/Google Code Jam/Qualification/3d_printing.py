"""
Full solution to the 3D Printing problem from Google Code Jam 2022 
Qualification Round.
"""



# Read number of tests.
n_tests = int(input())


# Empty lists for each colour.
cyan_list = []
magenta_list = []
yellow_list = []
black_list = []

def solve(test_count, cyan_list, magenta_list, yellow_list, black_list):
    """
    Given four lists (one for each colour) and number of test cases, solves the
    problem.
    """
    j = 0
    case_count = 1
    while (j < test_count * 3):
        if (j % 3 == 0):
            # Take sublists.
            cyan = cyan_list[j:j+3]
            magenta = magenta_list[j:j+3]
            yellow = yellow_list[j:j+3]
            black = black_list[j:j+3]

            # Get the minimum of the sublists.
            min_cyan = min(cyan)
            min_magenta = min(magenta)
            min_yellow = min(yellow)
            min_black = min(black)

            # Find the sum of the minima of the four lists.
            sum = min_cyan + min_magenta + min_yellow + min_black

            if (sum < 1e6):
                # Impossible if sum is less than 1 million.
                print(f"Case #{case_count}: IMPOSSIBLE")
            else:
                difference = sum - 1e6
                i = 0
                remaining_difference = int(difference)
                while (i < difference):
                    # Subtract min_difference / 4 from each colour if possible.
                    if (min_cyan > (remaining_difference // 4)):
                        min_cyan -= (remaining_difference // 4)
                        i += (remaining_difference // 4)
                        remaining_difference -= remaining_difference // 4
                    elif (min_magenta > (remaining_difference // 4)):
                        min_magenta -= (remaining_difference // 4)
                        i += (remaining_difference // 4)
                        remaining_difference -= remaining_difference // 4
                    elif (min_yellow > (remaining_difference // 4)):
                        min_yellow -= (remaining_difference // 4)
                        i += (remaining_difference // 4)
                        remaining_difference -= remaining_difference // 4
                    elif (min_black > (remaining_difference // 4)):
                        min_black -= (remaining_difference // 4)
                        i += (remaining_difference // 4)
                        remaining_difference -= remaining_difference // 4
                    
                    # Move in steps of 1.
                    if (min_cyan > 0 and remaining_difference > 0):
                        min_cyan -= 1
                        remaining_difference -= 1
                        i += 1
                    elif (min_magenta > 0 and remaining_difference > 0):
                        min_magenta -= 1
                        remaining_difference -= 1
                        i += 1
                    elif (min_yellow > 0 and remaining_difference > 0):
                        min_yellow -= 1
                        remaining_difference -= 1
                        i += 1
                    elif (min_black > 0 and remaining_difference > 0):
                        min_black -= 1
                        remaining_difference -= 1
                        i += 1
                    


                print(f"Case #{case_count}: {min_cyan} {min_magenta} {min_yellow} {min_black}")

            case_count += 1

        j += 1

def print_lists():
    """A debugging function."""
    print(f"cyan: {cyan_list}")
    print(f"magenta: {magenta_list}")
    print(f"yellow: {yellow_list}")
    print(f"black: {black_list}")


for i in range(n_tests * 3):
    # Read a line of numbers corresponding to amount of ink.
    inp = input().split()
    c = int(inp[0])
    m = int(inp[1])
    y = int(inp[2])
    k = int(inp[3])

    cyan_list.append(c)
    magenta_list.append(m)
    yellow_list.append(y)
    black_list.append(k)

# Solve the problem.
solve(n_tests, cyan_list, magenta_list, yellow_list, black_list)
