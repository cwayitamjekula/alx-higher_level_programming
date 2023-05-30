#!/usr/bin/python3
def magic_calculation(a, b):
    count = 0
    for i in range(1, 3):

        try:
            if i > a:
                raise Exception("Too far")
            count += (a ** b) / i
        except Exception:
            count = b + a
            break
        return count
