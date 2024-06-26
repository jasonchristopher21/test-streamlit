import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
    page_title="Singtel Phishing Dashboard",
    page_icon="👋",
)

report_options = [
    "Mar 2024 Phishing Campaign",
    "Aug 2023 Phishing Campaign",
    "Jun 2023 Phishing Campaign"
]

st.write("# View Reports")

st.write("### Select Report")

st.selectbox('Select Report to View', report_options)