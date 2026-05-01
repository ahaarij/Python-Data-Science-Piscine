import matplotlib.pyplot as plt
from load_csv import load


def display_country_life_expectancy(country: str, data) -> None:
    assert country in data["country"].values, f"The country '{country}' does not exist in the dataset"
    
    country_data = data[data["country"] == country]

    assert len(country_data.values) > 0 and len(country_data.values[0]) > 1 and len(country_data.columns) > 1, \
    f"Not enough data to display life expectancy of {country}"

    years = country_data.columns[1:]
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.title(country + " Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.xticks(years[::40])
    plt.show()


def main():
    try:
        data = load("life_expectancy_years.csv")

        display_country_life_expectancy("United Arab Emirates", data)

    except AssertionError as e:
        print("Assertion Error:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()