#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        weight = 0
        den = 0
        ave = 0
        
        for n in range(len(my_list)):
            for i in range(len(my_list[n])):
                weight += my_list[n][0] * my_list[n][1]
                den += my_list[n][1]
        ave = weight / den
        return ave
    return 0