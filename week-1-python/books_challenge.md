# Books Dataset Cleaning Challenge

## Overview
This challenge simulates a real-world data cleaning task, similar in scope and difficulty to a technical assessment previously completed in May 2025.

You are given a dataset called `books.csv` containing metadata about published books. Your task is to write a function that loads the data and performs several data cleaning operations.

---

## Dataset Columns
The CSV file includes the following columns:
- `title` – title of the book
- `author` – name of the author
- `year_published` – year the book was published
- `publisher` – name of the publishing house
- `price` – price of the book in USD
- `language` – language in which the book is written

---

## Instructions

Write a function named `process_books()` that:

1. Loads the file `books.csv` using encoding `'latin-1'`
2. Drops any rows where `title`, `author`, or `year_published` are missing
3. Filters the DataFrame to keep only books published in or after 2010
4. Normalizes the `language` column to lowercase (e.g., "English" → "english")
5. Creates a new column called `is_english`, which is `True` if the language is `"english"` and `False` otherwise
6. Returns the cleaned DataFrame with the index reset

---

## Goal
This exercise is designed to evaluate your understanding of:
- DataFrame loading and encoding
- Row filtering and column conditionals
- Data transformation and feature creation
- Pandas best practices

---
