import pandas as pd

def process_books():
    """
    Cleans and transforms a dataset of published books.

    Steps performed:
    1. Load data from 'books.csv' using latin-1 encoding.
    2. Drop rows missing 'title', 'author', or 'year_published'.
    3. Keep only books published in or after 2010.
    4. Normalize the 'language' column to lowercase.
    5. Create a boolean column 'is_english' where True if language == 'english'.
    6. Return the cleaned DataFrame with reset index.
    """
    books_df = pd.read_csv("books.csv", encoding="latin-1")

    books_df = books_df.dropna(subset=["title", "author", "year_published"])
    books_df = books_df[books_df["year_published"] >= 2010]
    books_df["language"] = books_df["language"].str.lower()
    books_df["is_english"] = books_df["language"] == "english"

    return books_df.reset_index(drop=True)

Add books_solution.py – refactored challenge logic
