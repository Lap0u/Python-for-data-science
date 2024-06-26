#!/usr/bin/env python3

import sys
import string


def text_analyzer(text=None):
    # Docstring syntax
    """Counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    try:
        while text is None:
            text = input("Please enter the string to count\n")
            print(text, "is the text", len(text))
    except EOFError:
        print("You can't fool me")
        return
    if isinstance(text, str) is False:
        print(f"{text} is not a string")
        return
    print(f"The text contains {len(text)} character(s):")

    # Add 1 for each uppercase letter and prints it
    print(f"- {sum(1 for elem in text if elem.isupper())} upper letter(s)")

    # Add 1 for each lowercase letter and prints it
    print(f"- {sum(1 for elem in text if elem.islower())} lower letter(s)")

    # Add 1 for each character from text included in string.punctuation
    punctuation = sum(1 for elem in text if elem in string.punctuation)
    print(f"- {punctuation} punctuation mark(s)")

    # Count spaces
    count = text.count(" ") + text.count("\r")
    print(f"- {count} space(s)")

    # Add 1 for each digit in text
    print(f"- {sum(1 for elem in text if elem.isdigit())} digit(s)")


def main():
    assert len(sys.argv) < 3, "more than one argument is provided"
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()


if __name__ == "__main__":
    main()
