"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    3. diagonal string
    Filename: diagonal_string.py
    Write a function called diagonal_string that takes a string as a parameter
    and returns each letter diagonally on a new line. For example, the call
    diagonal_string("northeastern") would return the string
    n
     o
      r
       t
        h
         e
          a
           s
            t
             e
              r
               n
"""


def diagonal_string(word):
    # takes a string
    # returns each letter diagonally on a new line
    if len(word) <= 1:
        return word
    new_str = ''
    i = 0
    while i < len(word) - 1:
        temp_str = (i * ' ') + word[i] + '\n'
        new_str = new_str + temp_str
        i += 1

    new_str = new_str + (len(word) - 1) * ' ' + word[-1]
    return new_str
