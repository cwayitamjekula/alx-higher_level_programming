#!/usr/bin/python3
def best_score(a_dictionary)
    if a_dictionary:
        sList = list(a_dictionary)
        sLarg = sList[0]
        for n in sList:
            if a_dictionary[sLarg] < a_dictionary[n]:
                sLarg = n
        return sLarg
    else:
        return
