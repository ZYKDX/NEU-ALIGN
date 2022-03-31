"""
    CS5001-5003 Spring 2022
    Coding practice module 4
    YUKUN ZHOU
    9. Debug
    Filename: debug.py
    Consider the provided code:

    def main():
        hi = int(input("Enter larger: "))
        lo = hi
        while lo >= hi:
            lo = int(input("Enter smaller: "))
        while lo < hi:
            print(lo)
            lo += 1
    main()

    The code should read in two integers from the keyboard where the second is
    strictly less than the first. Once the two numbers have been entered, it prints
    numbers starting from the high number all the way down to the low number(including)
    the low number. Again, the code isn't right. Your task should you choose to accept
    it, is to fix the code so that it does what it should do. Submit your solution
    of the corrected code.
"""


def main():
    hi = int(input("Enter larger: "))
    lo = hi
    while lo >= hi:
        lo = int(input("Enter smaller: "))

    while lo < hi:
        print(hi)
        hi -= 1
    print(lo)


if __name__ == '__main__':
    main()
