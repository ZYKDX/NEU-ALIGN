"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    10. Remove break
    Filename: remove_break.py
    Take a moment to run the provided code and determine what it does

    def main():
    a = 0
    b = 1
    print("0\n1")
    while True:
        c = a + b
        print(c)
        a = b
        b = c
        if c > 1000:
            break;
    main()

    Once you understand what it is doing, refactor the code so that it's
    functionality remains the same but so that it does not use a break statement
"""


def main():
    a = 0
    b = 1
    c = a + b
    print("0\n1")
    while c <= 1000:
        print(c)
        a = b
        b = c
        c = a + b


if __name__ == '__main__':
    main()
