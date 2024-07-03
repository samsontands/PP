import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():
    st.set_page_config(page_title="CSV Profiler", page_icon="📊", layout="wide")
    
    st.title("📊 CSV Profiler")
    st.write("Upload a CSV file to generate a pandas profiling report.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        @st.cache_data
        def load_csv():
            return pd.read_csv(uploaded_file)

        df = load_csv()
        st.write("Data Preview:")
        st.dataframe(df.head())

        if st.button("Generate Profiling Report"):
            pr = ProfileReport(df, explorative=True)
            st_profile_report(pr)

if __name__ == "__main__":
    main()
