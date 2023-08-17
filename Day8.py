import pandas as pd


def main():
    """Input:
    Users table:
    +---------+-----------+-------------------------+
    | user_id | name      | mail                    |
    +---------+-----------+-------------------------+
    | 1       | Winston   | winston@leetcode.com    |
    | 2       | Jonathan  | jonathanisgreat         |
    | 3       | Annabelle | bella-@leetcode.com     |
    | 4       | Sally     | sally.come@leetcode.com |
    | 5       | Marwan    | quarz#2020@leetcode.com |
    | 6       | David     | david69@gmail.com       |
    | 7       | Shapiro   | .shapo@leetcode.com     |
    +---------+-----------+-------------------------+
    Output:
    +---------+-----------+-------------------------+
    | user_id | name      | mail                    |
    +---------+-----------+-------------------------+
    | 1       | Winston   | winston@leetcode.com    |
    | 3       | Annabelle | bella-@leetcode.com     |
    | 4       | Sally     | sally.come@leetcode.com |
    +---------+-----------+-------------------------+
    """
    data = [
        [1, "Winston", "winston@leetcode.com"],
        [2, "Jonathan", "jonathanisgreat"],
        [3, "Annabelle", "bella-@leetcode.com"],
        [4, "Sally", "sally.come@leetcode.com"],
        [5, "Marwan", "quarz#2020@leetcode.com"],
        [6, "David", "david69@gmail.com"],
        [7, "Shapiro", ".shapo@leetcode.com"],
    ]
    Users = pd.DataFrame(data, columns=["user_id", "name", "mail"]).astype(
        {"user_id": "int64", "name": "object", "mail": "object"}
    )
    print(valid_emails(Users))
    pass

    """
Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
 

Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.

The result format is in the following example.
   """


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"
    valid_users = users[users["mail"].str.fullmatch(regex)]
    return valid_users.sort_values(by="user_id")


if __name__ == "__main__":
    main()
