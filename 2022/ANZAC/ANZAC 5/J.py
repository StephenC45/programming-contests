"""
Solution to Problem J (Joining Jargon) from 2022 ANZAC 5.
"""



subject = input()

vowels = "AEIOUaeiou"

# Iterate backwards to find the last vowel.
index = len(subject) - 1
while subject[index] not in vowels:
    index -= 1

# Take everything up to and including the last vowel, then add "ntry".
subject = subject[:index + 1]
subject += "ntry"

print(subject)
