#!/usr/bin/env python3

import sys


def filterwords(str: str, max_len: int):
    """Returns the words in the string that are
    longer than the maxLen argument"""
    split_str = str.split(" ")
    print([word for word in split_str if len(word) > max_len])


if __name__ == "__main__":
    assert len(sys.argv) == 3, "the arguments are bad"
    str = sys.argv[1]
    assert sys.argv[2].isdigit(), "the arguments are bad"
    max_len = int(sys.argv[2])
    filterwords(str, max_len)
