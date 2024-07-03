import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():
    st.set_page_config(page_title="Data Profiler", page_icon="📊", layout="wide")

    st.title("📊 Data Profiler")

    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", ["Upload Data", "View Profile"])

    if page == "Upload Data":
        st.header("Upload Your Data")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.session_state['df'] = df
            st.success("Data uploaded successfully!")
            st.dataframe(df.head())

    elif page == "View Profile":
        st.header("Data Profile")
        if 'df' in st.session_state:
            df = st.session_state['df']
            st.info("Generating profile report... This may take a moment.")
            pr = ProfileReport(df, explorative=True)
            st_profile_report(pr)
        else:
            st.warning("Please upload a CSV file first.")

if __name__ == "__main__":
    main()
