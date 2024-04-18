#!/usr/bin/env python3

import time


def get_eta(nums, pos, start: time):
    """Returns the estimated time of arrival"""
    if pos != 0:
        avg = (time.time() - start) / pos
        eta = round(avg * ((len(nums) - pos)), 2)
        minutes = int(eta // 60)
        seconds = int(eta % 60)
        return f"{minutes:02}:{seconds:02}"
    else:
        return "None"


def get_total(nums, pos):
    """Returns the total number of elements and the current position"""
    return f"{pos}/{len(nums)}"


def get_elpased(start: time):
    """Returns the time elapsed since the start of the program"""
    elapsed = time.time() - start
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    return f"{minutes:02}:{seconds:02}"


def print_loading(total, eta, elapsed, percent):
    """Prints a progress bar with the percentage of completion, the total"""
    if percent == 0:
        equals = ""
    else:
        equals = "█" * int(percent * 102 / 100)
    space = " " * (102 - len(equals))
    ##
    bar = equals + space + "|"
    print(
        f"{percent:n}%|{bar} {total} | [{elapsed}<{eta}]",
        end="\r",
    )


def ft_tqdm(lst: range) -> None:
    """Prints a progress bar for an iterable object"""
    start = time.time()
    for elem in lst:
        pos = lst.index(elem) + 1
        elapsed = get_elpased(start)
        eta = get_eta(lst, pos, start)
        total = get_total(lst, pos)
        percent = round(pos * 100 / len(lst))
        print_loading(total, eta, elapsed, percent)
        yield elem


# from time import sleep
# from tqdm import tqdm
# from Loading import ft_tqdm

# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()
# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()
