#!/usr/bin/python3


def sum_item_5(item):
    return item + 5

def my_list_factory(my_list):
    return [sum_item_5(item) for item in my_list if item % 2 == 0]

print(my_list_factory([1, 2, 3, 4]))
