from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Plots the distribution of life expectancy in France."""
    df = load("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
