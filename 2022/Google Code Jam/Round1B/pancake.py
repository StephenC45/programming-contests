"""
Full solution to the Pancake Deque problem from Google Code Jam 2022 Round 1B.

The most important idea is to dequeue the pancake with least deliciousness.

I made some really silly mistakes here. When I saw that I got 25 points on the
leaderboard, I wasn't aware that hidden verdict test sets would show up as
passed no matter what the result was, so I thought I had passed it. I was also
dumb enough to think that list slicing was O(1). It's not.

This full solution was written after the end of the round after realising the
above mistakes. My actual submission used list slicing and only passed the first
two out of three test sets, failing the third with time limit exceeded.
"""



# Read the number of test cases.
n_tests = int(input())
input_list = [] # Stores lists of pancake deliciousness values.
pancake_count_list = [] # Stores the pancake count for each test case.
#pancake_count = 0 (unused)


def solve(test_count, input_list):
    j = 0
    case_count = 1
    while (j < test_count):
        # Get the number of pancakes, and store the double ended queue
        # boundaries in lower_queue and upper_queue.
        pancake_count = pancake_count_list[j]
        lower_queue = 0
        upper_queue = pancake_count - 1

        #print(f"There are {pancake_count} pancakes.")
        max_delicious = 0
        paying_customers = 0

        while (pancake_count > 0):
            if (int(input_list[j][lower_queue]) < int(input_list[j][upper_queue])):
                # Dequeue from the left side.
                delicious = int(input_list[j][lower_queue])
                lower_queue += 1
            else:
                # Dequeue from the right side.
                delicious = int(input_list[j][upper_queue])
                upper_queue -= 1

            #print(f"Dequeued {delicious} from deque")
            #print(input_list[j])
            #print(f"Queue boundaries: {lower_queue}, {upper_queue}")

            if (delicious >= max_delicious):
                paying_customers += 1
                max_delicious = delicious
            
            pancake_count -= 1

        #print(f"There are {paying_customers} paying customers.")

        print(f"Case #{j + 1}: {paying_customers}")

        j += 1


for i in range(n_tests):
    inp2 = int(input())
    pancake_count_list.append(inp2)

    inp = input().split()
    input_list.append(inp)

    #print(input_list)
    #print(pancake_count_list)


solve(n_tests, input_list)

