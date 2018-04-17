<<<<<<< HEAD
"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nwelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("guess a number: "))
        print("you guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
=======
"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nwelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("guess a number: "))
        print("you guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
>>>>>>> 54705da028649df1326ec70bc41b0484469a2b54
