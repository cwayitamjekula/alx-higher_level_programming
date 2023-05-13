#!/usr/bin/python3
"""printing numbers from 0 to 99"""

for n in range(0, 100):
    if n == 99:
        print(n)
    else:
        print("{:0>2d}".format(n), end=", ")
