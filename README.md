# Python Data Cleaning CLI Tool

## Project Description

A beginner-friendly Python project that loads a local CSV file, inspects it, cleans common data quality issues (missing values, duplicates, whitespace), and saves a cleaned CSV. The same cleaning logic is also demonstrated in a Jupyter notebook and a simple Streamlit web demo.

### Learning Topics
- Python data structures
- pandas DataFrames
- NumPy array operations
- Basic data loading and data cleaning

## Objectives

- Load and inspect a CSV dataset with pandas
- Detect and handle missing values
- Remove duplicate rows
- Clean column names and text values
- Use median for numeric imputation and mode for categorical imputation
- Practice simple NumPy operations
- Visualize data with Matplotlib
- Build a simple command-line tool and a Streamlit demo

## Technologies Used

- Python 3
- pandas
- NumPy
- Matplotlib
- Streamlit
- Jupyter Notebook

## Features

- CLI tool that accepts a CSV path as a command-line argument
- Dataset inspection (shape, columns, dtypes, missing values, duplicates)
- Removal of completely empty rows and columns
- Duplicate row removal
- Column name and text whitespace cleaning
- Missing value imputation (median for numeric, mode for categorical)
- Cleaning summary and verification
- Cleaned CSV export
- Jupyter notebook walkthrough of the same steps plus visualizations
- Streamlit app for uploading, cleaning, and downloading a CSV

## Project Structure

```
python-data-cleaning-cli/
│
├── data/
│   └── laptopData.csv
│
├── data_cleaner.py      # CLI application
├── app.py               # Streamlit demo
├── data_cleaning.ipynb  # Learning notebook
├── cleaned_data.csv     # Output (generated after running)
├── requirements.txt
└── README.md
```

## Installation

1. Open a terminal in the project folder.
2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run the CLI

```bash
python data_cleaner.py data/laptopData.csv
```

The program will:
1. Check that the file exists
2. Load the CSV
3. Print inspection information
4. Clean the data
5. Save `cleaned_data.csv` in the current directory
6. Print the full path of the cleaned file

### Example Output (summary)

- Number of rows and columns
- Column names and data types
- Missing-value counts
- Number of missing values handled
- Original vs cleaned shape
- Path to the saved cleaned CSV

## How to Run the Streamlit Application

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

In the app you can:
1. Upload a CSV file
2. Preview the data and see shape / missing values
3. Click **Clean Dataset**
4. View a short cleaning summary
5. Preview the cleaned data
6. Download the cleaned CSV

## Example Commands

```bash
# Run the CLI on the provided dataset
python data_cleaner.py data/laptopData.csv

# Run the Streamlit demo
streamlit run app.py

# Open the notebook (from the project folder)
jupyter notebook data_cleaning.ipynb
```

## Data Cleaning Operations Performed

1. Check that the input file exists and is a readable CSV
2. Load data into a pandas DataFrame
3. Display rows, columns, column names, data types, and missing-value counts
4. Remove completely empty rows and columns
5. Remove duplicate rows
6. Strip whitespace from column names
7. Strip leading/trailing whitespace from text (object) columns
8. Detect numeric vs categorical columns
9. Impute missing values:
   - Numeric → median
   - Categorical/text → mode
10. Report how many missing values were handled and verify the result
11. Save the cleaned dataset as `cleaned_data.csv`

## Notebook Description

`data_cleaning.ipynb` walks through the same workflow step by step:

1. Import libraries (pandas, NumPy, Matplotlib)
2. Load the dataset and show the first rows
3. Understand the data (`head`, `shape`, `columns`, `info`, `describe`, dtypes)
4. Data quality analysis (missing values, duplicates, unique counts)
5. Cleaning steps with short explanations
6. Simple NumPy practice (array from Price, mean/median/min/max, basic arithmetic)
7. 4 meaningful Matplotlib charts (brand counts, type counts, price histogram, average price by type)
8. Before vs after comparison
9. Export `cleaned_data.csv`

## Expected Output

After running the CLI or the notebook:

- A file named `cleaned_data.csv` is created
- Empty rows are removed
- Duplicate rows are removed
- Missing values are filled (median / mode)
- Column names and text fields have no extra whitespace
- The cleaned file has fewer (or equal) rows than the original and zero missing values in the columns that could be imputed

## Learning Outcomes

By completing this project you will be able to:

- Load CSV data with `pd.read_csv()` and work with DataFrames
- Inspect data quality (missing values, duplicates, dtypes)
- Apply basic cleaning steps in a clear order
- Choose median vs mode for imputation and explain why
- Use NumPy for simple numeric calculations on a column
- Create basic charts with Matplotlib
- Build a small CLI tool that takes a file path from the user
- Reuse the same cleaning functions inside a Streamlit app
