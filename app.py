import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Title of the Streamlit app
st.title("Titanic Dataset Profiling")

# Load the dataset
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

# Generate the profile report
pr = ProfileReport(df, title="Pandas Profiling Report")

# Display the profile report in Streamlit
st_profile_report(pr)
