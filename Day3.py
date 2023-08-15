import pandas as pd


def main():
    testTable = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4, 5],
            "name": ["John", "Jane", "Joe", "Janet", "Jack"],
        }
    )
    testTable2 = pd.DataFrame({"customer_id": [1, 2, 3, 4], "order_id": [1, 2, 3, 4]})
    result = find_customers(testTable, testTable2)
    print(result)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    no_orders_df = customers[~customers["customer_id"].isin(orders["customer_id"])][
        ["name"]
    ]
    no_orders_df.columns = ["Customers"]
    return no_orders_df


if __name__ == "__main__":
    main()
