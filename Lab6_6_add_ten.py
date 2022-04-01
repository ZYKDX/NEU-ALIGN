"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    6. Add 10
    Filename: add_ten.py
    Write a function called add_ten that receives a list of integer
    values and adds 10 to each element in the list. The list should
    then be returned.
"""


def add_ten(my_list):
    if my_list == []:
        return my_list
    for i in range(len(my_list)):
        my_list[i] += 10
    return my_list
