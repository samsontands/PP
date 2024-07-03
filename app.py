import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

def main():
    st.title("Data Profiler")
    st.write("Upload your CSV file to generate a profile report.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display the first few rows of the dataset
        st.subheader("Dataset Preview")
        st.write(df.head())

        # Generate the profile report
        st.subheader("Generating Profile Report...")
        pr = ProfileReport(df, explorative=True)

        # Display the report
        st_profile_report(pr)

if __name__ == "__main__":
    main()
