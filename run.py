# import gspread
# from google.oauth2.service_account import Credentials

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
# ]

"""
Every google account has an IAM configuration.
IAM stands for Identity and Access Management.
This configuration specifies what the user has acces to.
The SCOPE lists the APIs that the program should access in order to run
"""

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('love_sandwiches')


# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data)


import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

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

def  get_sales_data():
    """
    Get sales figures input from the user
    """
    print('Please enter sales data from the last market.')
    print('Data should be six numbers, separated by commas.')
    print('Example: 10, 20, 30, 40, 50, 60\n')

    data_str = input('Enter your data here: ')

    sales_data = data_str.split(',')
    validate_data(sales_data)


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

get_sales_data()
