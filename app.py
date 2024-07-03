import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

# Load the dataset
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

# Generate the profiling report
pr = df.profile_report()

# Display the profiling report in the Streamlit app
st.title("Pandas Profiling Report")
st_profile_report(pr)
