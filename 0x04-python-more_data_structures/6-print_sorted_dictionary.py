#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedList = sorted(a_dictionary.keys())
    for n in sortedList:
        print("{:s}: {}".format(n, a_dictionary[n]))
