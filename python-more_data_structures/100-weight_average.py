#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    total_wight = 0
    for i in range(len(my_list)):
        mul = my_list[i][0] * my_list[i][1]
        total_wight += my_list[i][1]
        total += mul
    return total / total_wight
