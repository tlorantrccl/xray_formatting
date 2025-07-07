# xray_formatting
Overview:

This tool is a simple Python-based CSV formatter. It reads a user-supplied CSV file, applies your custom formatting rules, and writes out a corrected version alongside the original.

⸻

Features:
<br>
• One-click executable: No Python install required—just download and double-click.<br>
• Interactive file selection: Windows File Explorer pops up so you can pick the CSV to fix.<br>
• Automatic output naming: The fixed file is saved next to the original, with  (fixed) appended to its name.<br>

⸻

Prerequisites:

• Windows 10 or later<br>
• No additional libraries needed (all bundled into the executable)<br>

⸻

Installation:

1. Download the latest release ZIP or installer package for Windows.<br>
2. Unzip (if necessary) and place the executable (csv_formatter.exe) wherever you like—e.g., your Desktop or a dedicated utilities folder.<br>

⸻

Usage:
1. Launch:<br>
    • Double-click csv_formatter.exe.<br>
    • A brief console window will appear.<br>
2. Select your file:<br>
    • After a few seconds, a File Explorer dialog opens.<br>
    • Navigate to and click the CSV file you wish to reformat.<br>
    • Click Open.<br>
3. Wait:<br>
    • When done, it closes automatically.<br>
4. Find the output:<br>
    • In the same folder as your original file, you’ll now see <original_name> (fixed).csv.<br>
    • Open or import this file as you normally would.<br>

⸻

Troubleshooting:

- Nothing happens when I double-click<br>
    - Ensure the file extension is .exe.<br>
    - Try right-click → Run as administrator to rule out permission issues.<br>
- File Explorer doesn’t open<br>
    - Wait 5–10 seconds after launch; the script needs a moment to initialize.<br>
- I get an error about invalid CSV<br>
    - Check that your file is plain text, uses commas as delimiters, and has a .csv extension.<br>
- Output file didn’t appear<br>
    - Search the same folder for files ending in (fixed).csv.<br>
    - If it’s not there, re-run the tool and watch for any console errors before it closes.<br>

If the program is not working as expected shoot me an email to: tlorant@rccl.com