import pandas as pd


def main():
    id = [1, 2, 3]
    salary = [100, 200, 300]
    n = 2
    employee = pd.DataFrame({"id": id, "salary": salary})
    print(nth_highest_salary(employee, n))

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
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.
   """


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)

    if N > len(sorted_salaries):
        return pd.DataFrame({"Nth Highest Salary": [None]})

    nth_highest = sorted_salaries.iloc[N - 1]

    return pd.DataFrame({"Nth Highest Salary": [nth_highest]})


if __name__ == "__main__":
    main()
