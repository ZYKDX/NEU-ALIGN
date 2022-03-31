"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    5. String Equality
    Filename: string_eauqlity.py
    Write a program that reads in a word from
    the keyboard and prints "Hi, how are you"
    and "Done" if someone enters the word "Hi"
    (capitalization matters). Otherwise it just
    prints "Done". For example,

    Hi
    Hi, how are you?
    Done

    Bye
    Done
"""


def main():
    word = input('')

    if word == 'Hi':
        print('Hi, how are you?')
        print('Done')
    else:
        print('Done')


if __name__ == '__main__':
    main()
