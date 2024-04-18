#!/usr/bin/env python3


def ft_filter(function_to_apply, list_of_inputs):
    """ft_filter(function or None, iterable) --> filter object\n\n
    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true."""
    return [word for word in list_of_inputs if function_to_apply(word)]


# returns True if the argument passed is even
def check_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if an element passed to check_even() returns True, select it
even_numbers_iterator = ft_filter(check_even, numbers)

print("Even numbers are:", even_numbers_iterator)

letters = ["a", "b", "d", "e", "i", "j", "o"]


# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        return True
    else:
        return False


# selects only vowel elements
filtered_vowels = ft_filter(filter_vowels, letters)

print("Vowels are:", filtered_vowels)
