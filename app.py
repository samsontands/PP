import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import time

st.title('Data Profiling with YData Profiling')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    with st.spinner('Reading CSV file...'):
        df = pd.read_csv(uploaded_file)
        st.write(df)
        
    with st.spinner('Generating profiling report...'):
        profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
        
        # Save the report to an HTML file
        profile.to_file("profiling_report.html")
        
    st.success('Report generated successfully!')
    
    # Read the HTML file and display it
    with open("profiling_report.html", "r", encoding="utf-8") as file:
        report_html = file.read()
    
    st.components.v1.html(report_html, height=800, scrolling=True)

    # Provide a download button for the HTML file
    with open("profiling_report.html", "rb") as file:
        btn = st.download_button(
            label="Download Profiling Report",
            data=file,
            file_name="profiling_report.html",
            mime="text/html"
        )
