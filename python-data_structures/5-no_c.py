#!/usr/bin/python3
def no_c(my_string):
    total_C = my_string.count("c") + my_string.count("C")
    while total_C != 0:
        index = my_string.find("c")
        if index == -1:
            index = my_string.find("C")
        total_C -= 1
        my_string = my_string[:index] + my_string[index + 1:]
    return my_string
