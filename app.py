"""
Simple Streamlit demo for the Data Cleaning CLI Tool.
Uses the same cleaning functions from data_cleaner.py.
"""

import streamlit as st
import pandas as pd
import io
from data_cleaner import clean_dataframe, inspect_data

st.set_page_config(page_title="Data Cleaning Demo", layout="centered")
st.title("Data Cleaning Demo")
st.write("Upload a CSV file to clean it. This app uses the same logic as the CLI tool.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        if df.empty:
            st.error("The uploaded file is empty.")
        else:
            st.subheader("Uploaded Dataset Preview")
            st.dataframe(df.head(10))

            st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

            st.subheader("Missing Values")
            missing = df.isnull().sum()
            st.write(missing[missing > 0] if missing.sum() > 0 else "No missing values found.")
            st.write(f"Total missing: {missing.sum()}")
            st.write(f"Duplicate rows: {df.duplicated().sum()}")

            if st.button("Clean Dataset"):
                cleaned_df, summary = clean_dataframe(df.copy())

                st.subheader("Cleaning Summary")
                st.write(f"- Original shape: {summary['original_shape']}")
                st.write(f"- Cleaned shape: {summary['cleaned_shape']}")
                st.write(f"- Missing values handled: {summary['missing_handled']}")
                st.write(f"- Remaining missing: {summary['remaining_missing']}")
                st.write(f"- Duplicates removed: {summary['original_duplicates']}")

                st.subheader("Cleaned Dataset Preview")
                st.dataframe(cleaned_df.head(10))

                csv_buffer = io.StringIO()
                cleaned_df.to_csv(csv_buffer, index=False)
                st.download_button(
                    label="Download Cleaned CSV",
                    data=csv_buffer.getvalue(),
                    file_name="cleaned_data.csv",
                    mime="text/csv",
                )

    except Exception as e:
        st.error(f"Could not process the file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
