"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    9. Positional elements
    Filename: positional_elements.py
    Write a function called positional_elements that returns how many
    elements in the argument list have a value that is equal to the
    index of that element. In other words, the value 1 is found at index 1.
    You can ignore the fact that python supports negative indices
    (for example: list[-1] represents the last element in the list)
"""


def positional_elements(my_list):
    count = 0
    for i in range(len(my_list)):
        if i == my_list[i]:
            count += 1
    return count
