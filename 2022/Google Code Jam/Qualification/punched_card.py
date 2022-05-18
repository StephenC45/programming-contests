"""
Full solution to the Punched Cards problem from Google Code Jam 2022 
Qualification Round.
"""



# Read number of tests.
n_tests = int(input())

g_width = []
g_height = []

def print_cards(test_count, width_list, height_list):
    for j in range(test_count):
        lines_count = 0
        grid_height = height_list[j]
        width = width_list[j]
        column = 0

        print(f"Case #{j + 1}:")
        for i in range(grid_height):
            line = ""
            if (lines_count < 2):
                line = line + ".."
                if (lines_count % 2 == 0):
                    line = line + "+"
                    line = line + ((width - 1) * "-+")
                else:
                    line = line + "|"
                    line = line + ((width - 1) * ".|")
            else:
                if (lines_count % 2 == 0):
                    line = line + "+"
                    line = line + (width * "-+")
                else:
                    line = line + "|"
                    line = line + (width * ".|")

            print(line)
            lines_count += 1


for i in range(n_tests):
    inp = input().split()
    height = int(inp[0])
    width = int(inp[1])

    g_height.append(2 * height + 1)
    g_width.append(width)

    lines_count = 0
    column = 0

print_cards(n_tests, g_width, g_height)
    





