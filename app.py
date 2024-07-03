import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

def main():
    st.title("Data Profiling with Pandas Profiling")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)
        st.write("Dataset Preview:")
        st.write(df.head())

        # Generate and display the profile report
        pr = gen_profile_report(df, explorative=True)
        with st.expander("REPORT", expanded=True):
            st_profile_report(pr)
    else:
        st.write("Please upload a CSV file to generate a profile report.")

@st.cache_data
def gen_profile_report(df, *report_args, **report_kwargs):
    return df.profile_report(*report_args, **report_kwargs)

if __name__ == "__main__":
    main()
