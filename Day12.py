import pandas as pd 

"""
   Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.
   """
 
def main(): 
   data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
   Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
   data = [[1, 'IT'], [2, 'Sales']]
   Department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
   print(department_highest_salary(Employee, Department))

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
   employee_departement_df = pd.merge(employee, department, left_on='departmentId', right_on='id')
   max_salary_employees_df = employee_departement_df.groupby('name_y')['salary'].max().reset_index()
   max_salary_employees_df = pd.merge(max_salary_employees_df, employee_departement_df, left_on=['name_y', 'salary'], right_on=['name_y', 'salary'])
   max_salary_employees_df = max_salary_employees_df[['name_y', 'name_x', 'salary']]
   max_salary_employees_df = max_salary_employees_df.rename(columns={'name_x':'Employee', 'name_y':'Department', 'salary':'Salary'})
   return max_salary_employees_df
 
if __name__ == "__main__": 
   main() 
 
