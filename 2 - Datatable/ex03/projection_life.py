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


def merge_dataframes(df1, df2):
    """Merges two dataframes on their index."""
    condition_df1 = df1.index.isin(df2.index)
    df1_filtered = df1[condition_df1]
    condition_df2 = df2.index.isin(df1_filtered.index)
    df2_filtered = df2[condition_df2]
    return df1_filtered, df2_filtered


def main():
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")
    gdp.set_index("country", inplace=True)
    life_expectancy.set_index("country", inplace=True)
    gdp, life_expectancy = merge_dataframes(gdp, life_expectancy)
    gdp_1900 = gdp["1900"]
    life_expectancy_1900 = life_expectancy["1900"]
    xticks = [300, 1000, 10000]
    xticks_labels = ["300", "1k", "10k"]
    plt.scatter(gdp_1900, life_expectancy_1900, alpha=0.5)
    plt.xlabel("GDP per country")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks(xticks, xticks_labels)
    plt.title("Life expectancy vs GDP per country in 1900")
    plt.show()


if __name__ == "__main__":
    main()
