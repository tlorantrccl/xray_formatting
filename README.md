# xray_formatting
Overview
This tool is a simple Python-based CSV formatter. It reads a user-supplied CSV file, applies your custom formatting rules, and writes out a corrected version alongside the original.
⸻
Features
• One-click executable: No Python install required—just download and double-click.
• Interactive file selection: Windows File Explorer pops up so you can pick the CSV to fix.
• Automatic output naming: The fixed file is saved next to the original, with  (fixed) appended to its name.
⸻
Prerequisites
• Windows 10 or later
• No additional libraries needed (all bundled into the executable)
⸻
Installation
1. Download the latest release ZIP or installer package for Windows.
2. Unzip (if necessary) and place the executable (csv_formatter.exe) wherever you like—e.g., your Desktop or a dedicated utilities folder.
⸻
Usage
1. Launch
• Double-click csv_formatter.exe.
• A brief console window will appear (“Initializing…”).
2. Select your file
• After a few seconds, a File Explorer dialog opens.
• Navigate to and click the CSV file you wish to reformat.
• Click Open.
3. Wait
• The console window shows progress messages (e.g., “Reading…”, “Formatting…”, “Writing…”).
• When done, it closes automatically.
4. Find the output
• In the same folder as your original file, you’ll now see <original_name> (fixed).csv.
• Open or import this file as you normally would.
⸻
Troubleshooting
• Nothing happens when I double-click
    • Ensure the file extension is .exe.
    • Try right-click → Run as administrator to rule out permission issues.
• File Explorer doesn’t open
    • Wait 5–10 seconds after launch; the script needs a moment to initialize.
• I get an error about invalid CSV
    • Check that your file is plain text, uses commas as delimiters, and has a .csv extension.
• Output file didn’t appear
    • Search the same folder for files ending in (fixed).csv.
    • If it’s not there, re-run the tool and watch for any console errors before it closes.

If the program is not working as expected shoot me an email to: tlorant@rccl.com