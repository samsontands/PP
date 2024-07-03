import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

def main():
    st.title("Pandas Profiling in Streamlit")

    # Load the data
    df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

    # Generate the profile report
    profile = ProfileReport(df, title="Pandas Profiling Report")

    # Display the report in Streamlit
    st_profile_report(profile)

if __name__ == "__main__":
    main()
