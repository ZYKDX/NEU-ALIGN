"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    8. Pairs
    Filename: pairs.py
    Write a program that reads four integers from the keyboard and prints
    "two pairs" if the input consists of two matching pairs (in some order)
    and "not two pairs" otherwise. For example:

    1 2 2 1  two pairs
    1 2 2 3  not two pairs
    2 2 2 2  two pairs
"""


def main():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    c = int(input('Enter third number: '))
    d = int(input('Enter fourth number: '))

    if a == b and c == d:
        print('two pairs')
    elif a == c and b == d:
        print('two pairs')
    elif a == d and b == c:
        print('two pairs')
    else:
        print('not two pairs')


if __name__ == '__main__':
    main()
