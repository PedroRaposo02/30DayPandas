import pandas as pd


def main():
    testTable = pd.DataFrame(
        {
            "employee_id": [1, 2, 3, 4, 5, 6],
            "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
            "salary": [100, 200, 300, 400, 500, 600],
        }
    )
    testResult = pd.DataFrame(
        {
            "employee_id": [1, 2, 3, 4, 5, 6],
            "bonus": [100, 0, 300, 0, 500, 0],
        }
    )
    print("Test Table:")
    print(testTable)
    print("Expected Output:")
    print(testResult)
    print("Actual Output:")
    print(calculate_special_bonus(testTable))
    """
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 

Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The result format is in the following example.
   """  # noqa: E501


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0;
    
    employees.loc[(employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')),'bonus'] = employees['salary']
    
    result_df = employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])
    
    return result_df


if __name__ == "__main__":
    main()
