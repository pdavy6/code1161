# -*- coding: UTF-8 -*-

"""Week 3.



Modify each function until the tests pass.

"""









def loop_ranger(start, stop=None, step=1): 

    """Return a list of numbers between start and stop in steps of step.



    Do this using any method apart from just using range()

    """

    

    n_list = []

    number_a = start

    number_b = stop

    while number_a < number_b:

        n_list.append(number_a)

        number_a += step #this saves the value of step, updates counter

    return n_list

    





def lone_ranger(start, stop, step):

    """Duplicate the functionality of range.



    Look up the docs for range() and wrap it in a 1:1 way

    """

    l1_list = []

    number_a = start

    number_b = stop

    step_1 = step

    while number_a < number_b:

        l1_list.append(number_a)

        number_a += step_1

    return l1_list



def two_step_ranger(start, stop):

    """Make a range that steps by 2.



    Sometimes you want to hide complexity.

    Make a range function that always has a step size of 2

    """

    l2_list = []

    number_a = start

    number_b = stop

    step_2 = 2

    while number_a < number_b:

        l2_list.append(number_a)

        number_a += step_2

    return l2_list





def gene_krupa_range(start, stop, even_step, odd_step):

    """Make a range that has two step sizes.



    make a list that instead of having evenly spaced steps

    has odd steps be one size and even steps be another.

    """

    n_list = []

    number_a = start

    number_b = stop

    odd = odd_step

    even = even_step

    counter = 1

    while number_a < number_b:

        n_list.append(number_a)

        if counter % 2 == 1:

            number_a += odd

            counter += 1

        else:

            number_a += even

            counter += 1



    return n_list





def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.



    Ask for a number, and if the response is outside the bounds keep asking

    until you get a number that you think is OK

    """
    guessed = False
    while not guessed:
        guessed_n = int(input('input a number between {} and {}: '.format(low, high)))
        print('your input is {},'.format(guessed_n))
        if guessed_n < low or guessed_n > high:
            print('this number is not in range, please try again,')
        else:
            print('this number is in range, good bye...')
            guessed = True
    return guessed_n   
    





def not_number_rejector(message):

    while True:

        try:

            guessedNumber = int(input("Enter a number: "))

            a_number = int(guessedNumber)

            return a_number

        except ValueError:

            print("Sorry, that is not an integer, please try again: ")

    return



"""Ask for a number repeatedly until actually given one.



    Ask for a number, and if the response is actually NOT a number (e.g. "cow",

    "six", "8!") then throw it out and ask for an actual number.

    When you do get a number, return it.

    """

    





def super_asker(low, high):   

    guessed = False

    while not guessed:

        try:

            guessed_n = int(input('input a number between {} and {}: '.format(low, high)))

            print('your input is {},'.format(guessed_n))

        except ValueError:

            print("this input is not an integer, please try again: ")

            continue

        if guessed_n < low or guessed_n > high:

            print('this number is not in range, please try again,')

        else:

            print('this number is in range, good bye...')

            guessed = True

    return guessed_n


    

    """Robust asking function.



    Combine stubborn_asker and not_number_rejector to make a function

    that does it all!

    """







if __name__ == "__main__":

    # this section does a quick test on your results and prints them nicely.

    # It's NOT the official tests, they are in tests.py as usual.

    # Add to these tests, give them arguments etc. to make sure that your

    # code is robust to the situations that you'll see in action.

    # NOTE: because some of these take user input you can't run them from

    



    print("\nloop_ranger", loop_ranger(1, 10, 2))

    print("\nlone_ranger", lone_ranger(1, 10, 3))

    print("\ntwo_step_ranger", two_step_ranger(1, 10))

    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))

    print("\nstubborn_asker")

    stubborn_asker(30, 45)

    print("\nnot_number_rejector")

    not_number_rejector("Enter a number: ")

    print("\nsuper_asker")

    super_asker(33, 42)

