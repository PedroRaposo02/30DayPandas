import pandas as pd


def main():
    data = [[1, 100], [2, 200], [3, 300]]
    Employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
        {"id": "int64", "salary": "int64"}
    )
    print(second_highest_salary(Employee))

    """
   Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.
   """


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)
    second_highest_salary = (
        sorted_salaries.iloc[1] if len(sorted_salaries) > 1 else None
    )
    return pd.DataFrame({"SecondHighestSalary": [second_highest_salary]})


if __name__ == "__main__":
    main()
