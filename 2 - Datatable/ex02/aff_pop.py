from load_csv import load
import matplotlib.pyplot as plt


def convert_units(s):
    """Converts val with units such as M or k or B to its litteral val"""
    if s[-1] == "M":
        return int(float(s[:-1]) * 10**6)
    if s[-1] == "k":
        return int(float(s[:-1]) * 10**3)
    if s[-1] == "B":
        return int(float(s[:-1]) * 10**9)
    return int(s)


def main():
    """Plots the population in France vs Belgium over the years."""
    df = load("population_total.csv")
    df.set_index("country", inplace=True)
    for col in df.columns:
        df[col] = df[col].apply(convert_units)
    france = df.loc["France"]
    belgium = df.loc["Belgium"]
    ticks_x = [x for x in df.columns if int(x) % 40 == 0]
    ticks_y = [20_000_000, 40_000_000, 60_000_000]
    ticks_y_labels = ["20M", "40M", "60M"]
    plt.plot(belgium, label="Belgium")
    plt.plot(france, label="France")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population projections")
    plt.xticks(ticks_x)
    plt.yticks(ticks_y, ticks_y_labels)
    plt.legend()
    plt.xlim(["1800", "2050"])
    plt.show()


if __name__ == "__main__":
    main()
