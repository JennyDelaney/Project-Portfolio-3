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


def get_customer_name():
    """
    Get Customers name ordering the cake
    """
    print("Welcome to Jessie's Bakery\n")
    print("Please give a name for the cake order\n")

    name_str = input("Enter your name here:")
    print(f"The name of the customer is {name_str}\n")


def get_customer_number():
    """
    Get Customers telephone number for the order
    """

    print("Please confirm a contact telephone number for the order\n")
    
    phone_num_str = input("Enter your telephone number here:")
    print(f"The telephone number given is {phone_num_str}\n")


get_customer_name()
get_customer_number()