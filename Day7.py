import pandas as pd 
 
def main(): 
   test_df = pd.DataFrame(
         {
               "user_id": [1, 2, 3],
               "name": ["aLiCe", "BOB", "charLie"],
            }
      )
   fix_names(test_df)

   """
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The result format is in the following example.
"""

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
   users['name'] = users['name'].str.capitalize()
   return users.sort_values(by=['user_id'])
 
if __name__ == "__main__": 
   main() 
 
