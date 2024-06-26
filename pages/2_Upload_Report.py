import streamlit as st
import pandas as pd
from io import StringIO

st.write("""
# Create New Report

Upload Excel file to start creating a new report.
""")

st.write("#### Campaign Name")

st.text_input("Campaign Name", placeholder="Enter Campaign Name", label_visibility="collapsed")

st.write("#### Upload Report")

st.write("Don't have the Report Template? Download it [here!](https://google.com)")

uploaded_file = st.file_uploader("Choose a file", label_visibility="collapsed")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)
    st.write(f"{df.shape[0]} rows x {df.shape[1]} columns")
    st.button("Process file")
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)

