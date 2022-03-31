"""
    CS5001-5003 Spring 2022
    Coding practice module 3
    YUKUN ZHOU
    7. Grade
    Filename: grade.py
    Using the grade scale for this class (that you can find on the syllabus)
    write a function called grade that receives a score and returns the letter
    grade for that score
"""


def grade(score):
    if score >= 93:
        return 'A'
    elif score >= 90:
        return 'A-'
    elif score >= 86:
        return 'B+'
    elif score >= 82:
        return 'B'
    elif score >= 77:
        return 'B-'
    elif score >= 73:
        return 'C+'
    elif score >= 69:
        return 'C'
    elif score >= 65:
        return 'C-'
    else:
        return 'F'
