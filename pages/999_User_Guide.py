import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Singtel Phishing Dashboard",
    page_icon="👋",
)

report_options = [
    "Mar 2024 Phishing Campaign",
    "Aug 2023 Phishing Campaign",
    "Jun 2023 Phishing Campaign"
]

st.write("# User Guide")