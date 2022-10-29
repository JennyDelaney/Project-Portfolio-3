import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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


def number_cake_layers():
    print("How many layers would you like the cake to be?\n")
    print("Please choose between - 1,2,3 or 4\n")

    cake_layers_str = input("Please enter the no. of layers you would like:")
    print(f"You have chosen to have a {cake_layers_str} layered cake.\n")


def cake_size():
    print("You have the following options for the size of cake - ")
    sizes = SHEET.worksheet("options").get_all_values()
    sizes_data = sizes[0]
    print(sizes_data)
    
def main():
    """
    Run all program functions
    """ 
    get_customer_name()
    get_customer_number()
    number_cake_layers()
    cake_size()

print("Welcome to Jessie's Bakery Ordering System\n")
main()