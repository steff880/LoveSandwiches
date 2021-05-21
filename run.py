import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


"""
Every google account has an IAM configuration.
IAM stands for Identity and Access Management.
This configuration specifies what the user has acces to.
The SCOPE lists the APIs that the program should access in order to run
"""

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data)

"""
The foramt that we are going to expect our values in is called csv.
It stands for comma separated values and it is a very basic file type,
which allows data to be saved in a table structured format.
We can imagine that our love sandwiches machine prints out data
at the end of the day.
"""


def get_sales_data():
    """
    Get sales figures input from the user
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print('Please enter sales data from the last market.')
        print('Data should be six numbers, separated by commas.')
        print('Example: 10, 20, 30, 40, 50, 60\n')

        data_str = input('Enter your data here: ')

        sales_data = data_str.split(',')

        if validate_data(sales_data):
            print('Data is valid!')
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all strings into integers.
    Raises ValueError if string cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True

# def update_sales_worksheet(data):
#     """
#     Update sales worksheet, add new row with the list data provided.
#     """
#     print('Updating sales worksheet...\n')
#     sales_worksheet = SHEET.worksheet('sales')
#     sales_worksheet.append_row(data)
#     print('Sales worksheet updated successfully.\n')

# def update_surplus_worksheet(data):
#     """
#     Updates the surplus worksheet with data provided
#     """
#     print('Updating the surplus worksheet...\n')
#     surplus_worksheet = SHEET.worksheet('surplus')
#     surplus_worksheet.append_row(data)
#     print('Surplus worksheet updated successfully.\n')


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worsheet with data provided
    """

    print(f'Updating the {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet.capitalize()} worksheet updated successfully.\n')


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus idicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print('Calculating surplus data...\n')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    surplus_data = []
    """
    Use zip() method to iterate through two lists at the same time.
    """
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def get_last_5_entry_sales():
    """
    Collects columns of data from each sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists
    """
    sales = SHEET.worksheet('sales')
   
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')


print('Welcome to Love Sandwiches Data Automation')

# main()

sales_columns = get_last_5_entry_sales()
