"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    5. Read words
    Filename: read_words.py
    Write a program that prompts the user with Enter a word: and reads words in
    from the keyboard. After it is done reading words, it should print all the
    words in a single line with single spaces between them. The word stop should
    not be included. For example:

    Enter a word: nine
    Enter a word: total
    Enter a word: whatever
    Enter a word: stop
    nine total whatever
"""


def main():
    all_words = ''
    new = input('Enter a word: ')
    while new != 'stop':
        all_words = all_words + new + ' '
        new = input('Enter a word: ')
    print(all_words)


if __name__ == '__main__':
    main()
