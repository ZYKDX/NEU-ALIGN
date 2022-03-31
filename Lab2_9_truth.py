"""
    CS5001-5003 Spring 2022
    Coding practice module 2
    YUKUN ZHOU
    9. Truth
    Filename: truth.py
    Write a program that completes and prints out the following truth table.
    Recall from this module that a truth table contains all of the possible
    combination of p, q and r. You should use the | - and + to build the lines
    in the table

    p r q A B
    F F F ? ?
    F F T ? ?
    F T F ? ?
    F T T ? ?
    T F F ? ?
    T F T ? ?
    T T F ? ?
    T T T ? ?

    where the ? in columns A and B are calculated as:
    A = (p and q) or not r
    B = not(p and (q or not r))
"""


def tf(var):
    if var == True:
        return 'T'
    else:
        return 'F'

def main():
    
    print('+---+---+---+---+---+')
    print('| p | q | r | A | B |')
    print('+---+---+---+---+---+')
    p,q,r = False, False, False
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| F | F | F | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = False, False, True
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| F | F | T | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = False, True, False
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| F | T | F | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = False, True, True
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| F | T | T | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = True, False,False
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| T | F | F | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = True, False, True
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| T | F | T | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = True, True, False
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| T | T | F | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
    p,q,r = True, True, True
    A = (p and q) or not r
    B = not(p and (q or not r))
    print('| T | T | T | ', tf(A), ' | ', tf(B), ' |', sep = '')
    print('+---+---+---+---+---+')
   


if __name__ == '__main__':
    main()
