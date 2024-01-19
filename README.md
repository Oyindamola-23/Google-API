# Kelani's Ventures Gas Sales Analysis

This Python script utilizes the gspread library to interact with Google Sheets API, fetching data from a specific Google Sheet for analysis. The analysis focuses on various sheets related to the operations and financials of Kelani's Ventures and it provides interactive reporting based on user-entered codes.

## Prerequisites

- Python 3.x
- Installed libraries:
    - gspread
    - oauth2client
    - pandas

## Google Sheets Setup

1. Share the Google Sheet with the service account email address specified in the credentials file.
2. Ensure the sheet contains the following columns:
    - CODE
    - TOTAL GAS KG SOLD
    - TOTAL AMOUNT SOLD
    - TOTAL AMOUNT BOUGHT
    - PROFIT (Gas)
    - NET PROFIT

## Authentication

1. Download the service account credentials file (JSON) and place it in the same directory as the script.

## Running the Script

1. Execute the script using Python:

   ```bash
   python gas_sales_analysis.py


2. Follow the prompts to enter codes and view sales data.

## Analysis

The script performs the following actions:

  Authenticates with the Google Sheets API using service account credentials.
  Opens the specified Google Sheet by URL and title.
  Retrieves data from selected sheets into a Pandas DataFrame for analysis.
  Converts specified numeric columns to numeric types.
  Allows interactive analysis by entering codes within the range A to O.
  Displays total gas sold for the entered code if data is found.

## Sheets for Analysis

Dashboard/month
Dashboard/50kg
Financials/month
Financials/50kg
Monthly Sales/month
Monthly Sales/50kg
Daily CIT
Inventory
Gas Operating Cost/month
Gas Operating Cost/50kg
Utility Operating Cost/month
Utility Operating Cost/50kg
Database

## Usage

Run the script.
Enter a code (A to O) for interactive analysis.
Type 'exit' to quit the analysis loop.

## Functionality

- Retrieves data from the specified Google Sheet.
- Converts relevant columns to numeric types for calculations.
- Prompts the user to enter a code between A and O.
- Calculates and displays the total gas sold for the entered code.
- Allows the user to enter multiple codes or type "exit" to quit.

## Additional Notes

- The script currently analyzes data from the "Dashboard/ 50kg" sheet. Adjust the `sheet_name` variable if needed.
- Error handling for missing columns or invalid codes is included.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- Name: Kelani Sidikat Oyindamola
- Email: kelanisidikat883@gmail.com
