"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    8. Find value
    Filename: find_value.py
    Write a recursive function called find_value that takes in a list of strings
    and a target value and returns whether the target value is in the list of strings
"""


def find_value(mylist, myvalue):
    # a list of strings and a target value
    # returns whether the target value is in the list
    if mylist == []:
        return False
    if myvalue == mylist[0]:
        return True
    if myvalue != mylist[0]:
        if len(mylist) == 1:
            return False
        else:
            return find_value(mylist[1:], myvalue)
