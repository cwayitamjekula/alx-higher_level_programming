#!/usr/bin/python3
"""printing numbers from 0 to 99"""

for numbers in range(0, 100):
    if numbers >= 0 and numbers < 99:
        print("{:02d}".format(numbers), end=", ")
    if numbers == 99:
        print("99")
