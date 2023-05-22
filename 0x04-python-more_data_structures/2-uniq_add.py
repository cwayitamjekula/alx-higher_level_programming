#!/usr/bin/python3

#uniq_add adds unique integers to list
def uniq_add(my_list=[])
    unique = set(my_list)
    uniqueList = list(unique)
    sum = 0

    for n in uniqueList:
        sum += n
    return sum
