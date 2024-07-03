import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

@st.cache_resource
def generate_profile_report(df, *report_args, **report_kwargs):
    return ProfileReport(df, *report_args, **report_kwargs)

def main():
    st.set_page_config(page_title="CSV Profiler", page_icon="📊", layout="wide")
    
    st.title("📊 CSV Profiler")
    st.write("Upload a CSV file or use the default Titanic dataset to generate a pandas profiling report.")

    # Option to use default dataset or upload a file
    data_option = st.radio("Choose data source:", ("Use default Titanic dataset", "Upload your own CSV"))

    if data_option == "Use default Titanic dataset":
        dataset_url = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
        df = load_data(dataset_url)
        st.write(f"🔗 [Titanic dataset]({dataset_url})")
    else:
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = load_data(uploaded_file)
        else:
            st.warning("Please upload a CSV file.")
            return

    st.write("Data Preview:")
    st.dataframe(df.head())

    if st.button("Generate Profiling Report"):
        with st.spinner("Generating report..."):
            pr = generate_profile_report(df, explorative=True)
        with st.expander("REPORT", expanded=True):
            st_profile_report(pr)

if __name__ == "__main__":
    main()
