"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    7. Compare lists
    Filename: compare_lists.py
    Write a function called compare_lists that receives two lists of integer
    values. The function should return true if all of the elements in the
    first list are contained in the second list (but not necessarily in the
    same order).
"""


def compare_lists(list_1, list_2):
    for i in list_1:
        if i in list_2:
            continue
        else:
            return False
    return True
