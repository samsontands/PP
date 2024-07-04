import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

st.title('Data Profiling with YData Profiling')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
    st.write(profile.to_html(), unsafe_allow_html=True)
