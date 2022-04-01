"""
    CS5001-5003 Spring 2022
    Coding practice module 7
    YUKUN ZHOU
    10. Number of choices
    Filename: choose.py
    Combinatorics are an interesting subject in data science.
    One problem in combinatorics involves studying the number
    of different ways that k things can be selected from among
    n different choices. For example, if you are choosing among
    six desserts and are allowed to take two, then the number
    of different combinations you can choose is 15.
    Here's one formula to compute this value:  C(n,k) = n! / (n-k)!k!
    This value also gives rise to an interesting recursion:
    C(n,k) = C(n-1,k-1) + C(n-1,k)
    Write a recursive function called choose that computes the number of combinations
    possible given k and n (in that order) where n>=k>=0
"""


def choose(k, n):
    # n >= k >= 0
    # c(n,k)=c(n-1,k-1)+c(n-1,k)
    if n == 0 or k == 0:
        return 1
    if n == k:
        return 1
    return choose(k - 1, n - 1) + choose(k, n - 1)
