"""
    CS5001-5003 Spring 2022
    Coding practice module 5
    YUKUN ZHOU
    9. Fibonacci List
    Filename: fibonacci.py
    Write a function called fibonacci that takes a single
    positive integer value and returns a list that contains
    the first n Fibonacci numbers.
    The Fibonacci sequences starts 1, 1, 2, 3, 5, 8, ...
"""


def fibonacci(value):
    # takes a value
    # returns a list of the first n terms in the fib sequence
    fibo_ls = []
    if value == 1:
        fibo_ls = [1]
    elif value == 2:
        fibo_ls = [1, 1]
    elif value > 2:
        fibo_ls = [1, 1]
        i = 2
        while i < value:
            fibo_ls.append(fibo_ls[i - 1] + fibo_ls[i - 2])
            i += 1
    return fibo_ls
