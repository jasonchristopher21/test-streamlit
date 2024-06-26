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

st.write("# Send Emails")

st.write("Easily send emails to update the Phishing Report Progress")

st.write("## Emailing Options")

recipient_options = st.radio(
    "Select Recipients",
    [
        "My team",
        "All Group BU, Dept and Sub-Dept Heads",
        "Custom Recipients"
    ],
    captions = [
        "Only me and the selected members in my team. Useful for testing before sending actual emails",
        "Sends to all Group BU, Department and Sub-Department Heads specified in the uploaded data",
        "Specify custom recipients"
    ]
)

if recipient_options == "All Group BU, Dept and Sub-Dept Heads":
    st.warning("⚠️ **WARNING!** This will send email to all Group BU, Department and Sub-Department heads. \
               This action is irreversible. Proceed with caution")

if recipient_options == "Custom Recipients":
    st.text_area("Custom Recipients List (Enter one email per line)")

st.write('## Campaign')

selected_campaign = st.selectbox("Select campaign", options=report_options)

if selected_campaign != report_options[0]:
    st.warning("⚠️ **WARNING!** This is not the latest campaign. Proceed with caution")

st.write("## Email Template")

st.write("Select custom email template (accepts HTML)")

st.file_uploader("Select file")

st.write("or type email here!")

st.text_input("Email Subject")

st.text_area("Email Body")

st.button("Next")