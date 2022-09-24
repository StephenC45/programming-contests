"""
Full solution to the P@55w0rd problem.
https://www.hackerrank.com/contests/2022-annual-programming-competition-division-b/challenges/pa55w0rd

Scored 10 points.

If you are a UNSW student, take COMP2041 to understand regex. Challenging but
very useful course.
"""



import re

line1 = input().split()
N = int(line1[0])
M = int(line1[1])


def convert_password(password_str):
    """
    Performs substitutions to convert a password to all alphanumeric characters.
    """
    new_password = re.sub("@", "a", password_str)
    new_password = re.sub("3", "e", new_password)
    new_password = re.sub("[1!]", "i", new_password)
    new_password = re.sub("0", "o", new_password)
    new_password = re.sub("[5$]", "s", new_password)

    return new_password


# Read original password and convert it.
original_password_to_match = input().strip()
password_to_match = convert_password(original_password_to_match)

# Keep track of number of matches. Read passwords and convert them, if they are
# the same as password_to_match, print the original password.
match_count = 0
for i in range(N):
    possible_match = input().strip()
    if (convert_password(possible_match) == password_to_match):
        print(possible_match)
        match_count += 1

# No matches found.
if (match_count == 0):
    print("No matches")
