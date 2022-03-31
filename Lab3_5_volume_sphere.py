"""
    CS5001-5003 Spring 2022
    Coding practice module 3
    YUKUN ZHOU
    5. Volume of a sphere
    Filename: volume_sphere.py
    Write a function called volume_sphere that receives the radius of a sphere,
    and returns the volume of the sphere. For your implementation, assume PI = 3.14159
"""


def volume_sphere(radius):
    PI = 3.14159
    return (4 / 3) * PI * (radius ** 3)
