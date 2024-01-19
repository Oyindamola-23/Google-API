import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from time import sleep


# Authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\HP\\Downloads\\kelanis-ventures-cf762a2f80e6.json", scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/17ZXzLj79kIUDnHyMqEV2qoNZwhZ23d58DGTNfSawwgc/edit#gid=1229067739')

# Open the Google Sheet by its title
spreadsheet_title = "KELANI'S VENTURES"
spreadsheet = gc.open(spreadsheet_title)

# List of specific sheet
sheet_names = [
    "Dashboard/month",
    "Dashboard/50kg",
    "Financials/month",
    "Financials/50kg",
    "Monthly Sales/month",
    "Monthly Sales/50kg",
    "Daily CIT",
    "Inventory",
    "Gas Operating Cost/month",
    "Gas Operating Cost/50kg",
    "Utility Operating Cost/month",
    "Utility Operating Cost/50kg",
    "Database"
]

# Specify the sheet name for analysis
sheet_name = "Dashboard/ 50kg"
worksheet = spreadsheet.worksheet(sheet_name)

# Get all values from the sheet
values = worksheet.get_all_values()

# Create a DataFrame using pandas
df = pd.DataFrame(values[1:], columns=values[0])

# Print welcome message
print("Welcome to Kelani's Ventures, what do you want to know")

# Convert numeric columns to numeric types
numeric_columns = ["TOTAL GAS KG SOLD", "TOTAL AMOUNT SOLD", "TOTAL AMOUNT BOUGHT", "PROFIT (Gas)", "NET PROFIT"]

# Check if all columns exist in the DataFrame
missing_columns = [col for col in numeric_columns if col not in df.columns]
if missing_columns:
    print(f"Missing columns in DataFrame: {missing_columns}")
else:
     # Convert numeric columns to numeric types
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

# Make the analysis interactive
while True:
    code_input = input("Enter the code (or 'exit' to quit): ").strip().upper()

    if code_input == 'EXIT':
        break

    # Check if the entered code is within the range A-O
    if 'A' <= code_input <= 'O':
        # Filter DataFrame based on the entered code
        filtered_df = df[df['CODE'] == code_input]

        if not filtered_df.empty:
            # Calculate the total gas sold for the entered code
            total_gas_sold = filtered_df["TOTAL GAS KG SOLD"].sum()
            print(f"Total Gas Sold for Code '{code_input}': {total_gas_sold}")
        else:
            print(f"No data found for Code '{code_input}'")
    else:
        print("Invalid code. Please enter a code between A and O.")
