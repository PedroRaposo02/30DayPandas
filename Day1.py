import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world.loc[
        (world["area"] >= 3_000_000) | (world["population"] >= 25_000_000),
        ["name", "population", "area"],
    ]
    return df


def big_countries_query(world: pd.DataFrame) -> pd.DataFrame:
    df = world.query("area >= 3_000_000 or population >= 25_000_000")[
        ["name", "population", "area"]
    ]
    return df


def big_countries_where(world: pd.DataFrame) -> pd.DataFrame:
    df = world.where(
        (world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)
    ).dropna()[["name", "population", "area"]]
    return df


def big_countries_alt(world: pd.DataFrame) -> pd.DataFrame:
    big_countries_df = world[
        (world["area"] >= 3000000) | (world["population"] >= 25000000)
    ]
    result_df = big_countries_df[["name", "population", "area"]]
    return result_df


def main():
    # Name is the primary key (column with unique values) for this table.
    # Each row of this table gives information about the name of a country,
    # the continent to which it belongs, its area, the population, and its GDP value.
    # A country is big if:
    # it has an area of at least three million (i.e., 3000000 km2), or
    # it has a population of at least twenty-five million (i.e., 25000000).
    # Write a solution to find the name, population, and area of the big countries.
    # Return the result table in any order.
    # The result format is in the following example.

    data = [
        ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
        ["Albania", "Europe", 28748, 2831741, 12960000000],
        ["Algeria", "Africa", 2381741, 37100000, 188681000000],
        ["Andorra", "Europe", 468, 78115, 3712000000],
        ["Angola", "Africa", 1246700, 20609294, 100990000000],
    ]

    World = pd.DataFrame(
        data, columns=["name", "continent", "area", "population", "gdp"]
    ).astype(
        {
            "name": "object",
            "continent": "object",
            "area": "Int64",
            "population": "Int64",
            "gdp": "Int64",
        }
    )

    print(big_countries(World).to_string())


if __name__ == "__main__":
    main()
