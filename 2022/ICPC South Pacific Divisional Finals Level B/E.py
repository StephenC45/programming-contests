"""
Solution to Problem E (Eating Socks) from ICPC 2022 South Pacific Divisional 
Finals (Level B).

You need to print the number of types where there are an odd number of socks
of that type.

This solution uses a dictionary.
"""



sock_count = int(input())

number_dict = {}

line2 = input().split()
for i in line2:
    sock_num = int(i)
    if i not in number_dict:
        number_dict[i] = 1
    else:
        number_dict[i] += 1
    
missing_count = 0
for item in number_dict.keys():
    if (number_dict[item] % 2 != 0):
        missing_count += 1

print(missing_count)
