<<<<<<< HEAD
"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

from exercise1 import not_number_rejector
from exercise1 import super_asker

import random
def advancedGuessingGame():
  print("\nwelcome to the guessing game!")
  print("A number between _ and 100 ?")
  lowerBound = input("Enter an lower bound: ")
  print("OK then, a number between {} and 100 ?".format(lowerBound))
  lowerBound = int(lowerBound)
  highBound = 100
  
  actualNumber = random.randint(lowerBound, 100)

  guessed = False
  while not guessed:
    try:
      guessed_n = int(input('input a number between {} and {}: '.format(lowerBound, highBound)))
      print('your input is {},'.format(guessed_n))
    except ValueError:
      print("this input is not an integer, please try again: ")
      continue
    if guessed_n < lowerBound or guessed_n > highBound:
      print('this number is not in range stupid, please try again,')
    elif guessed_n == actualNumber:
      print("you got it!! It was {}".format(actualNumber))
      guessed = True
    elif guessed_n < actualNumber:
      print("too small, try again ")
    else:
      print("too big, try again   ")
  return "You got it!"



"""def advancedGuessingGame():
  print("\nwelcome to the guessing game!")
  print("A number between _ and 100 ?")
  lowerBound = input("Enter an lower bound: ")
  print("OK then, a number between {} and 100 ?".format(lowerBound))
  lowerBound = int(lowerBound)
  highBound = 100
  actualNumber = random.randint(lowerBound, 100)

  guessed = False
  while not guessed:
    try:
      guessedNumber = int(input("guess a number: "))
      print("you guessed {},".format(guessedNumber),)
    except ValueError:
      print("this input is not an integer, please try again: ")
      continue
    if guessedNumber < lowerBound:
      print('not in range stupid, you\'re the asshole that set the lowest number, please try again: ')
    elif guessedNumber > highBound:
      print('dumb-ass you know the number isn\'t higher than 100, please try again: ')
    elif guessedNumber == actualNumber:
      print("you got it!! It was {}".format(actualNumber))
      guessed = True
    elif guessedNumber < actualNumber:
      print("too small, try again ")
    else:
      print("too big, try again ")
    
  return guessedNumber"""

"""Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


if __name__ == "__main__":
    advancedGuessingGame()
=======
"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
>>>>>>> 54705da028649df1326ec70bc41b0484469a2b54
