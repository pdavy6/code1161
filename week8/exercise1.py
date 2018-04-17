# -*- coding: UTF-8 -*-
"""
I'm in UR exam.

This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.

You've have 90 minutes.
"""

import string 

def getLetter(index):
    alphabet = string.ascii_lowercase + " "
    return alphabet[index]

import time

def getLetter(index): 
    alphabet = time + " "
    return alphabet[index]

def greet(name="Towering Timmy"): 
    """Return a greeting.

    return a string of "Hello" and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    return "Hello " + str(Towering Timmy)


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.

    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    counter = 0
    for item in input_list:
        if item == 3:
            counter += 1
    return counter 


def fizz_buzz():
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
            from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special, and a string
    if it is. E.g. [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ...]
    """
    fizzBuzzList = []
    # your code here
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("Fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("Buzz")
        else:
            fizzBuzzList.append(i)
    return fizzBuzzList 
        
    


def put_behind_bars(input_string="very naughty boy"): 
    """Interleave the input_string with pipes.

    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return the string
    "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: conside using the 'join' method in Python.
    TIP: make sure that you have a pipe on both ends of the string.
    """
    broken = list(input_string)
    barred = [x+"|" for x in broken]
    return "|" + "".join(barred) 
     



def pet_filter(letter="a"):
    """Return a list of pets whose name contains the character 'letter'"""
    pets = ["dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken",
            "guinea pig", "donkey", "duck", "water buffalo",
            "western honey bee", "dromedary camel", "horse", "silkmoth",
            "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca",
            "guineafowl", "ferret", "muscovy duck", "barbary dove",
            "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi",
            "canary", "society finch", "fancy mouse", "siamese fighting fish",
            "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"]
    in_list = []
    for p in pets:
        if letter in p:
            in_list.append(p)
    return in_list 



def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string
    the_alphabet = string.ascii_lowercase
    best_letter = ""
    best_number = 0
    for letter in the_alphabet:
        count = len(pet_filter(letter))
        if count > best_number:
            best_number = count
            best_letter = letter
    return best_letter
    


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.

    There is a random word generator here:
    "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=3&maxLength=10&limit=1"
    Currently, minLength=3 and maxLength=10 in this url. 
    This means we will get a word between 3 and 10 characters.
    If we set minLength=7 and maxLength=7, we will get something like this:
    >>> url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=7&maxLength=7&limit=1"
    >>> r = requests.get(url)
    >>> r.json() # will get you a python list containing something like this:
    >>> # [{"id":5651391,"word":"salmony"}]
    
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    { 
        3: ['Sep', 'the', 'yob'],
        4: ['aaaa', 'bbbb', 'cccc'],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc']
    }
    Use the API to get the 3 words.
    
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library

    """
    
    import requests
    return
    word_dictionary = {}
    for number in range(3, 8):
        word_dictionary[number] = []
        for word in range(3):
           


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.

    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library, 
        see line 77 of week4/hangman_leadboard.py for an example.
    """
    import random
    pass


def fast_filler(number_of_words=200):
    """Reimplement random_filler_text.

    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run,if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.words"
    TIP: you'll need the os library
    TIP: you'll probably want to use json dumps and loads to get the dictionary
    into and out of the file. Be careful when you read it back in, it'll
    convert integer keys to strings.
    """
    pass


if __name__ == '__main__':
    print((greet()))
    print((three_counter()))
    print((fizz_buzz()))
    print((put_behind_bars()))
    print((pet_filter()))
    print((best_letter_for_pets()))
    print((make_filler_text_dictionary()))
    print((random_filler_text()))
    print((fast_filler()))
    for i in range(10):
        print((i, fast_filler()))
        
