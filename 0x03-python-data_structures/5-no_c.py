#!/usr/bin/python3
def no_c(my_string):
    newWord = ""
    for n in (my_string):
        if n == "C" or n == "c":
            continue
        newWord += n
    return newWord
