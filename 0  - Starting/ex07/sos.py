#!/usr/bin/env python3

import sys

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/",
}


def sos(str):
    """Converts a string to morse code and prints it"""
    upper = str.upper()
    translated = ""
    for letter in upper:
        translated += MORSE_CODE_DICT[letter]
        translated += " "
    # print without last space
    print(translated[:-1])


if __name__ == "__main__":
    assert len(sys.argv) == 2, "the arguments are bad"
    str = sys.argv[1]
    for letter in str:
        assert letter.isalnum() or letter.isspace(), "the arguments are bad"
    sos(str)
