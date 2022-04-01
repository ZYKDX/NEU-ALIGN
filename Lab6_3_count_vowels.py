"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    3. Count vowels
    Filename: count_vowels.py
    Write a function called count_vowels that takes a string as an input and
    returns the number of vowels (a,e,i,o,u) that are found in the sentence
"""


def count_vowels(my_string):
    count = 0
    for i in my_string:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1
    return count
