import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def fix_multiline_csv(path_in: str, path_out: str, sep: str = ";") -> None:
   # 1. Read all lines
   with open(path_in, encoding="utf-8") as f:
       lines = f.read().splitlines()
   # 2. Figure out expected number of fields from the header
   header = lines[0]
   expected_fields = header.count(sep) + 1
   # 3. Accumulate logical records
   fixed_lines = [header]

   buffer = ""
   
   for raw in lines[1:]:
       # start a new buffer if empty, else append with a space/newline if needed
       buffer = (buffer + " " + raw).lstrip() if buffer else raw
       # if this buffer now *has* exactly the expected fields, it’s a full record
       if buffer.count(sep) + 1 == expected_fields:
        buffer = buffer.replace('"', '')
        fixed_lines.append(buffer)
        buffer = ""   # reset for next record
   # 4. (Optional) Warn if any trailing buffer remains
   if buffer:
       print("Warning: leftover partial record:\n", buffer)
   # 5. Write the cleaned file
   with open(path_out, "w", encoding="utf-8", newline="\n") as f:
       f.write("\n".join(fixed_lines))

def clean_csv(in_csv):
    
# Usage
    #  in_csv  = "./Data/Test Executions Report 01-07-25 11_43_05.csv"\
    print("UF NAME: ", in_csv.name)
    out_csv = f"{in_csv.name}(fixed).csv"
    fix_multiline_csv(in_csv, out_csv)
    # 6. Now read with pandas normally
    df = pd.read_csv(out_csv, sep=";")

    # Separate the status of the different types of test cases form the status column
    test_cases = {"PASSED JIRA": 0,
                "TO DO JIRA": 0,
                "EXECUTING JIRA": 0,
                "FAILED JIRA": 0,
                "BLOCKED JIRA": 0,
                "N/A JIRA": 0,
                "TOTAL TEST": 0
                }

    new_columns = test_cases.keys()

    for col in new_columns:
        df[col] = np.zeros(len(df), dtype=int)
    
    for index, row in df.iterrows():
    #    print('ROW: ', row)
    #    print("AT: ", df.at[index, 'Status'], " INDEX: ", index)
    # Check the number of each type of status and store it in the dictionary

        if "PASSED" in df.at[index, "Status"]:
            passed_index = df.at[index, "Status"].find("PASSED: ") + 8
            number_index = df.at[index, "Status"].find(" ", passed_index)
            test_cases["PASSED JIRA"] = df.at[index, "Status"][passed_index : number_index]  
        if "TO DO" in df.at[index, "Status"]:
            todo_index = df.at[index, "Status"].find("TO DO: ") + 7
            number_index = df.at[index, "Status"].find(" ", todo_index)
            test_cases["TO DO JIRA"] = df.at[index, "Status"][todo_index : number_index]

        if "EXECUTING" in df.at[index, "Status"]:
            executing_index = df.at[index, "Status"].find("EXECUTING: ") + 11
            number_index = df.at[index, "Status"].find(" ", executing_index)
            test_cases["EXECUTING JIRA"] = df.at[index, "Status"][executing_index : number_index]

        if "FAILED" in df.at[index, "Status"]:
            failed_index = df.at[index, "Status"].find("FAILED: ") + 8
            number_index = df.at[index, "Status"].find(" ", failed_index)
            test_cases["FAILED JIRA"] =df.at[index, "Status"][failed_index : number_index]

        if "BLOCKED" in df.at[index, "Status"]:
            blcoked_index = df.at[index, "Status"].find("BLOCKED: ") + 9
            number_index = df.at[index, "Status"].find(" ", blcoked_index)
            test_cases["BLOCKED JIRA"] = df.at[index, "Status"][blcoked_index : number_index]
        if "N/A" in df.at[index, "Status"]:
            na_index = df.at[index, "Status"].find("N/A: ") + 5
            number_index = df.at[index, "Status"].find(" ", na_index)
            test_cases["N/A JIRA"] = df.at[index, "Status"][na_index : number_index]

        # Set the values to the dictonary value and rest the dictionary
        test_cases["TOTAL TEST"] = sum(int(test_cases[key]) for key in test_cases.keys())
        
        for key in test_cases.keys():
            df.at[index, key] = int(test_cases[key])
            test_cases[key] = 0

    

    df.drop('Status', axis=1, inplace=True)

    df.to_csv(out_csv, index=False)
    return df


# clean_csv(dataset)
