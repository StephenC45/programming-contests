"""
Solution to Problem B (Ultimate Binary Watch) from 2022 ANZAC 1.
"""



import math


def numtobit(n):
    """
    Given a string or integer n, converts n to an integer and returns a list
    containing the symbols to be printed according to the binary representation
    of the integer form of n.
    """
    # Declare empty list and convert the input to an integer.
    bits = []
    n = int(n)

    # Perform trial division using powers of 2, starting from 8 down to 1.
    for i in range(3, -1, -1):
        if (n // math.pow(2, i) == 0):
            # The bit is 0.
            bits.append('.')
        else:
            # The bit is 1.
            bits.append('*')
            n = n - math.pow(2, i)
        
    return bits

# Read the input number.
num = input()

# Stores the output from numtobit() and then use it later to print the output.
output = []

for i in num:
    # For each digit in the number, append its associated string of symbols.
    output.append(numtobit(i))

# Print what the ultimate binary watch would display.
for i in range(4):
    print(f"{output[0][i]} {output[1][i]}   {output[2][i]} {output[3][i]}")