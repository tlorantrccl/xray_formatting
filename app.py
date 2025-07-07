import streamlit as st
from fixing_xray import clean_csv

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select a file")

print("Selected File: ", file_path)


# To update the executable run this line in the terminal: pyinstaller --onefile --name=xray_test_executions_formating app.py

st.title("CSV Cleaner Tool (from home)")

uploaded_file = st.file_uploader("Upload CSV", type="csv")


if uploaded_file:
   st.success("File uploaded!")

   df_clean = clean_csv(uploaded_file)

   st.write("Cleaned Data Preview: ", df_clean.head())

   csv = df_clean.to_csv(index=False).encode('utf-8')
   st.download_button("Download Cleand CSV", csv, "cleaned.csv", "text/csv")

   # python -m PyInstaller --onefile --name xray_test_executions_formating --copy-metadata streamlit --recursive-copy-metadata streamlit --hidden-import importlib.metadata app.py