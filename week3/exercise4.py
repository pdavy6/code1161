# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
  n_list = []
  number_a = low
  number_b = high
  while number_a < number_b:
    n_list.append(number_a)
    number_a += actual_number
  return n_list
  
  first = low
  last = len(high) - 1
  found = False
  while (first <= last and not found):
    mid = (first + last) // 2
    if n_list[mid] == actual_number:
        found = True
    else:
           if n_list[mid] > actual_number:
               last = last-1
           else:
               first = first+1
  
  return found
  testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
  print(binarySearch(testlist, 3))
  print(binarySearch(testlist, 13))

"""Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """

#return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
