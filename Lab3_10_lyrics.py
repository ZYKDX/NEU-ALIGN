"""
    CS5001-5003 Spring 2022
    Coding practice module 3
    YUKUN ZHOU
    9. Lyrics
    Filename: lyrics.py
    Write a program (remember that programs have a main() function)
    to print the lyrics of the song "Old MacDonald". Your program should
    print the lyrics for five different animals (five verses), similar to
    the example verse below:
    
    Old MacDonald had a farm, ee-igh, ee-igh, oh!
    And on that farm he had a cow, ee-igh, ee-igh, oh!
    With a moo, moo here and a moo, moo there.
    Here a moo, there a moo, everywhere a moo, moo.
    Old MacDonald had a farm, ee-igh, ee-igh, oh!
"""


def lyrics(animal, sound):
    print("Old MacDonald had a farm, ee-igh, ee-igh, oh!")
    print("And on that farm he had a " + animal + ", ee-igh, ee-igh, oh!")
    print("With a " + sound + ", " + sound + " here and a ", end='')
    print(sound + ", " + sound + " there.")
    print("Here a " + sound + ", there a " + sound + ", everywhere a ", end='')
    print(sound + ", " + sound + ".")
    print("Old MacDonald had a farm, ee-igh, ee-igh, oh!")


def main():
    lyrics("chicken", "zhi")
    lyrics("cat", "meow")
    lyrics("dog", "wang")
    lyrics("duck", "gua")
    lyrics("bird", "gugu")


if __name__ == '__main__':
    main()
