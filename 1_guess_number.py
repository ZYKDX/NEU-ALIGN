"""
    YUKUN ZHOU
    03/03/2022
    Plays 'guess my number' game.
          1. human user secretly picks a number between 1 and 100
          2. computer guesses and asks 'is it 1?'
          3. yes - if the computer guess is right
             low - if the guess is too low
             high - if the guess is too high
          4. limited to 7 guesses, if higher than 7, then computer lose
"""


def main():
    
    print("Please secretly pick a number, and write it on a paper")
    lower = 1
    upper = 100
    count = 1
    guess = (lower + upper) // 2
    while count < 8:
        print("Is it ", guess, "?", sep = '')
        response = input()
        if response == 'yes':
            print("Computer win! The number is ", guess, ", and it takes ", count, " times!", sep = '')
            return 1
        elif response == 'low':
            lower = guess + 1
            guess = (lower + upper) // 2
            count += 1
        elif response == 'high':
            upper = guess - 1
            guess = (lower + upper) // 2
            count += 1
    print("Computer lose! ", count - 1, " times have been used up!", sep = '')
    return 0


if __name__ == '__main__':
    main()

            
