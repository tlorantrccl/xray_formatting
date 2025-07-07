import streamlit as st
from main import clean_csv

# To locally host the program with stream lit: streamlit run app.py

st.title("CSV Cleaner Tool (from home)")

uploaded_file = st.file_uploader("Upload CSV", type="csv")


if uploaded_file:
   st.success("File uploaded!")

   df_clean = clean_csv(uploaded_file)

   st.write("Cleaned Data Preview: ", df_clean.head())

   csv = df_clean.to_csv(index=False).encode('utf-8')
   st.download_button("Download Cleand CSV", csv, f"{uploaded_file.name[:-4]}(fixed).csv", "text/csv")

   # python -m PyInstaller --onefile --name xray_test_executions_formating --copy-metadata streamlit --recursive-copy-metadata streamlit --hidden-import importlib.metadata app.py