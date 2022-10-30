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
    print("Please give a name for the cake order")

    name_str = input("Enter your name here:")
    print(f"The name of the customer is {name_str}\n")


def get_customer_number():
    """
    Get Customers telephone number for the order
    """
    print("Please confirm a contact telephone number for the order")
    
    phone_num_str = input("Enter your telephone number here:")
    print(f"The telephone number given is {phone_num_str}\n")


def number_cake_layers():
    print("How many layers would you like the cake to be?\n")
    print("Please choose between - 1,2,3 or 4")

    cake_layers_str = input("Please enter the no. of layers you would like:")
    print(f"You have chosen to have a {cake_layers_str} layered cake.\n")


def cake_options():
    """
    Function to return the different options available from spreadsheet
    """
    print("You have the following options for the size of cake - ")

    options_ws = SHEET.worksheet("options").get_all_values()
    cake_sizes = [item[0] for item in options_ws]
    cake_sizes.pop(0)
    print(cake_sizes)
    size_str = input('The cake size I would like is - ')
    print(f"A {size_str} cake has been picked.\n")

    print("You have the following options for flavour of sponge - ")
    sponge_flavours = [item[1] for item in options_ws]
    sponge_flavours = sponge_flavours[1:]
    print(sponge_flavours)
    sponge_flav_str = input('The sponge flavour I would like is - ')
    print(f"You have picked a {sponge_flav_str} sponge flavour.\n")
    
    print("Which type of filling would you like - ")
    filling_types = [item[2] for item in options_ws]
    del filling_types[0]
    del filling_types[2:]
    print(filling_types)
    filling_str = input('The filling I would like is - ')
    print(f"You have picked a {filling_str} filling.\n")

    filling_flavours = [item[3] for item in options_ws]
    filling_flavours.pop(0)
    print(filling_flavours)
    

def main():
    """
    Run all program functions
    """ 
    get_customer_name()
    get_customer_number()
    number_cake_layers()
    cake_options()


print("Welcome to Jessie's Bakery Ordering System\n")
main()