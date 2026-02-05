#!/usr/bin/python3
"""Module for Pascal's Triangle functional logic."""


def pascal_triangle(n):
    """Generates a lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing the triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    big_list = [[1]]
    small_list = [1]
    tmp_list = []

    for i in range(1, n):
        tmp_list.append(small_list[0])
        for j in range(len(small_list) - 1):
            tmp_list.append(small_list[0 + j] + small_list[1 + j])
        tmp_list.append(small_list[-1])
        small_list = tmp_list.copy()
        big_list.append(small_list)
        tmp_list.clear()
    return big_list
