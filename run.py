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
SHEET = GSPREAD_CLIENT.open('Bakery_cake_orders')

def get_name_data():
    """
    Get Customers name ordering the cake
    """
    print("Welcome to Jessie's Bakery\n")
    print("Please give a name for the cake order")

    name_str = input("Enter your name here:")
    print(f"The name of the customer is {name_str}")

get_name_data()