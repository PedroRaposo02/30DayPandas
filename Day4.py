import pandas as pd

# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.

# The result format is in the following example.


# Example 1:

# Input:
# Views table:
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+
# Output:
# +------+
# | id   |
# +------+
# | 4    |
# | 7    |
# +------+


def main():
    table_views = pd.DataFrame(
        {
            "article_id": [1, 1, 2, 2, 4, 3, 3],
            "author_id": [3, 3, 7, 7, 7, 4, 4],
            "viewer_id": [5, 6, 7, 6, 1, 4, 4],
            "view_date": [
                "2019-08-01",
                "2019-08-02",
                "2019-08-01",
                "2019-08-02",
                "2019-07-22",
                "2019-07-21",
                "2019-07-21",
            ],
        }
    )
    pd.DataFrame({"id": [4, 7]})
    print(article_views(table_views))


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    own_article_viewer_df = views[views["author_id"] == views["viewer_id"]][
        ["author_id"]
    ]
    own_article_viewer_df.drop_duplicates(inplace=True)
    own_article_viewer_df.rename(columns={"author_id": "id"}, inplace=True)
    own_article_viewer_df.sort_values(by=["id"], inplace=True)

    return own_article_viewer_df


if __name__ == "__main__":
    main()
