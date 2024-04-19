from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plots the distribution of life expectancy in France."""
    df = load("life_expectancy_years.csv")
    france = df[df["country"] == "France"].iloc[0, 1:]
    columns = df.columns[1:]
    ticks = [x for x in columns if int(x) % 40 == 0]
    plt.plot(france)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy projections")
    plt.xticks(ticks)
    plt.show()


if __name__ == "__main__":
    main()
