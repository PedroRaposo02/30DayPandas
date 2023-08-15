import sys
import os
import pandas as pd


def main():
    pass


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    low_fats_recyclable_df = products[
        (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    ]
    return low_fats_recyclable_df[["product_id"]]


if __name__ == "__main__":
    main()
