"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    9. In English
    Filename: in_english.py
    Write a recursive function called in_english that takes a integer value as input
    and returns a string containing the digits of the number in English
    For example, in_english(153) would return "one five three"
"""


def in_english(n):
    # takes a int
    # return a string contain the digits of the number in English
    # in_english(153) return "one five three"
    library_1 = ['zero', 'one', 'two', 'three', 'four']
    library_2 = ['five', 'six', 'seven', 'eight', 'nine']
    library = library_1 + library_2
    if n < 10:
        return library[n]
    return in_english(n // 10) + ' ' + in_english(n % 10)
