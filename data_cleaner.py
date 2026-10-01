#!/usr/bin/env python3
"""
Simple Data Cleaning CLI Tool
Loads a CSV, inspects it, cleans missing values and duplicates, then saves the result.
"""

import sys
import os
import pandas as pd
import numpy as np


def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Could not read CSV file. Reason: {e}")

    if df.empty:
        raise ValueError("The dataset is empty.")

    return df


def inspect_data(df):
    """Print basic information about the dataset."""
    print("\n--- Dataset Inspection ---")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print(f"\nColumn names:\n{list(df.columns)}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values per column:\n{df.isnull().sum()}")
    print(f"\nTotal missing values: {df.isnull().sum().sum()}")
    print(f"Duplicate rows: {df.duplicated().sum()}")


def clean_column_names(df):
    """Remove leading/trailing whitespace from column names."""
    df.columns = df.columns.str.strip()
    return df


def remove_empty_rows_cols(df):
    """Remove rows and columns that are completely empty."""
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    return df


def clean_text_whitespace(df):
    """Strip leading/trailing whitespace from text columns."""
    text_cols = df.select_dtypes(exclude=[np.number]).columns
    for col in text_cols:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
    return df


def get_column_types(df):
    """
    Detect numeric and categorical columns.
    Numeric = int or float dtype.
    Categorical = everything else (object, string, etc.).
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()
    return numeric_cols, categorical_cols


def impute_missing(df):
    """
    Fill missing values:
    - Numeric columns → median
    - Categorical columns → mode
    Returns the cleaned DataFrame and the number of missing values that were filled.
    """
    missing_before = df.isnull().sum().sum()
    numeric_cols, categorical_cols = get_column_types(df)

    for col in numeric_cols:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)

    for col in categorical_cols:
        if df[col].isnull().any():
            mode_val = df[col].mode()
            if len(mode_val) > 0:
                df[col] = df[col].fillna(mode_val[0])

    missing_after = df.isnull().sum().sum()
    handled = missing_before - missing_after
    return df, handled


def clean_dataframe(df):
    """
    Full cleaning pipeline.
    Returns cleaned DataFrame and a small summary dictionary.
    """
    original_shape = df.shape
    original_missing = df.isnull().sum().sum()
    original_duplicates = df.duplicated().sum()

    df = clean_column_names(df)
    df = remove_empty_rows_cols(df)
    df = clean_text_whitespace(df)
    df = df.drop_duplicates()

    df, missing_handled = impute_missing(df)

    summary = {
        "original_shape": original_shape,
        "cleaned_shape": df.shape,
        "original_missing": original_missing,
        "missing_handled": missing_handled,
        "remaining_missing": df.isnull().sum().sum(),
        "original_duplicates": original_duplicates,
        "cleaned_duplicates": df.duplicated().sum(),
    }
    return df, summary


def save_cleaned(df, output_path="cleaned_data.csv"):
    """Save the cleaned DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    return os.path.abspath(output_path)


def main():
    if len(sys.argv) < 2:
        print("Usage: python data_cleaner.py <path_to_csv>")
        print("Example: python data_cleaner.py data/laptopData.csv")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        print(f"Loading file: {file_path}")
        df = load_csv(file_path)

        inspect_data(df)

        print("\n--- Starting data cleaning ---")
        cleaned_df, summary = clean_dataframe(df)

        print(f"\nMissing values handled: {summary['missing_handled']}")
        print(f"Remaining missing values: {summary['remaining_missing']}")
        print(f"Original shape: {summary['original_shape']}")
        print(f"Cleaned shape:  {summary['cleaned_shape']}")
        print(f"Duplicates removed: {summary['original_duplicates']}")

        if summary["remaining_missing"] == 0:
            print("Verification: All missing values have been handled successfully.")
        else:
            print("Warning: Some missing values could not be filled.")

        output_path = save_cleaned(cleaned_df)
        print(f"\nCleaned dataset saved to: {output_path}")

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
