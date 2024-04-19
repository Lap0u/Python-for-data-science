from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plots the population in France vs Belgium over the years."""
    df = load("population_total.csv")
    france = df[df["country"] == "France"].iloc[0, 1:]
    belgium = df[df["country"] == "Belgium"].iloc[0, 1:]
    for i in range(len(france)):
        france[i] = france[i][:-1]
        belgium[i] = belgium[i][:-1]
    print(france, france[1])
    print(belgium)
    columns = df.columns[1:]
    ticks_x = [x for x in columns if int(x) % 40 == 0]
    ticks_y = [20, 40, 60]
    plt.plot(belgium, label="Belgium")
    plt.plot(france, label="France")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population projections")
    plt.xticks(ticks_x)
    plt.yticks(ticks_y)
    plt.legend()
    plt.xlim(["1800", "2050"])
    plt.show()


if __name__ == "__main__":
    main()
