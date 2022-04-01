"""
    CS5001-5003 Spring 2022
    Coding practice module 6
    YUKUN ZHOU
    10. Count words
    Filename: count_words.py
    Write a program that reads in a sentence from the keyboard and prints
    each word on it's own line. For example,

    Enter a sentence: The cat in the hat
    0. The
    1. cat
    2. in
    3. the
    4. hat
"""


def main():
    sentence = input("Enter a sentence: ")
    word_list = sentence.split()
    for i in range(len(word_list)):
        print(i, '.', ' ', word_list[i], sep='')


if __name__ == '__main__':
    main()
