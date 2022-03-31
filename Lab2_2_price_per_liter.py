"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    2. Price per liter
    Filename: price_per_liter.py
    Suppose you are at the grocery store to buy soda and you want to get the best deal
    Write a program that reads in the price of a six-pack of soda and the price of a
    two-liter bottle. The program should print out the price per liter for both assuming
    that cans are 12 oz or 0.355 liters. For example:
    Price per six_pack: 2.75
    Price per two_liter: 1.74

    Six-pack price per liter: 1.2910798122065728
    Two-liter price per liter: 0.87
"""


def main():
    price_six = float(input("Price per six-pack: "))
    price_two = float(input("Price per two-liter: "))

    ppl_six = price_six / (0.355 * 6)
    ppl_two = price_two / 2

    print("Six-pack price per liter:", ppl_six)
    print("Two-liter price per liter:", ppl_two)


if __name__ == '__main__':
    main()
