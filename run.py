import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Bakery_cake_orders")


def get_customer_name():
    """
    Get Customers name ordering the cake
    """
    print("Please give a name for the cake order")

    while True:
        name_str = input("Enter your name here:")
        if not name_str.isalpha():
            print("Customer name must contain letters only\n")
            continue
        else:
            print(f"The name of the customer is {name_str}\n")
            break

    return name_str


def get_customer_number(name):
    """
    Get Customers telephone number for the order
    """
    print(f"{name}, please confirm a contact telephone number for the order")

    while True:
        phone_num_str = input("Enter your telephone number here:")
        if not phone_num_str.isdigit():
            print("Customer number must not contain letters\n")
            continue
        else:
            print(f"The telephone number given is {phone_num_str}\n")
            break

    return phone_num_str


def number_cake_tiers(name):
    """
    Get the number of tiers the customer would like the cake
    """
    options_ws = SHEET.worksheet("options").get_all_values()

    print(f"{name}, how many tiers would you like the cake to be?")
    print("Please choose between 1,2,3 or 4 tiers by typing 0, 1, 2 or 3")

    cake_tiers = [item[0] for item in options_ws]
    cake_tiers.pop(0)
    for i, cake_tier in enumerate(cake_tiers):
        print(i, cake_tier)
    while True:
        tier_num = input("The no of tiers I would like is option - ")
        tier_choice = int(tier_num)
        if tier_choice > 4:
            print("Invalid choice. Please choose option 0, 1, 2 or 3")
            continue
        else:
            print(f"You have chosen {cake_tiers[tier_choice]}\n")
            break

    return cake_tiers[tier_choice]


def cake_options(name, customer_number, number_tiers):
    """
    Function to return the different options available for the cake
    """
    options_ws = SHEET.worksheet("options").get_all_values()

    # Confirmation of cake size
    print("You have the following options for the size of cake - ")
    print("Please choose option 0, 1, 2 or 3")
    cake_sizes = [item[1] for item in options_ws]
    cake_sizes.pop(0)
    for i, cake_size in enumerate(cake_sizes):
        print(i, cake_size)
    while True:
        size = input("The cake size I would like is option - ")
        size_choice = int(size)
        if size_choice > 4:
            print("Invalid choice. Please choose size option 0, 1, 2 or 3")
            continue
        else:
            print(f"You have chosen a {cake_sizes[size_choice]} cake\n")
            break

    # Confirmation of sponge flavour
    print("You have the following options for flavour of sponge - ")
    sponge_flavs = [item[2] for item in options_ws]
    sponge_flavs = sponge_flavs[1:]
    for i, sponge_flav in enumerate(sponge_flavs):
        print(i, sponge_flav)
    while True:
        sponge_flav_str = input("Choose the sponge flavour - ")
        sponge_choice = int(sponge_flav_str)
        if sponge_choice > 4:
            print("Invalid choice. Please choose size option 0, 1, 2 or 3")
            continue
        else:
            print(f"You've picked a {sponge_flavs[sponge_choice]} sponge.\n")
            break

    # Confirmation of filling
    print("Which type of filling would you like - ")
    filling_types = [item[3] for item in options_ws]
    del filling_types[0]
    del filling_types[2:]
    for i, filling_type in enumerate(filling_types):
        print(i, filling_type)
    while True:
        filling_str = input("The filling I would like is number - ")
        filling_choice = int(filling_str)
        if filling_choice > 2:
            print("Invalid choice. Please choose size option 0, 1")
            continue
        else:
            print(
                f"You've picked a {filling_types[filling_choice]} filling.\n"
            )
            break

    # Confirmation of cake order
    print(f"{name}, {customer_number}: You have ordered the following cake - ")
    print(f"{number_tiers}, {cake_sizes[size_choice]}")
    print(f" {sponge_flavs[sponge_choice]} sponge")
    print(f" with {filling_types[filling_choice]}\n")


def main():
    """
    Run all program functions
    """
    name = get_customer_name()
    customer_number = get_customer_number(name)
    number_tiers = number_cake_tiers(name)
    cake_options(name, customer_number, number_tiers)


print("Welcome to Jessie's Bakery Ordering System\n")
main()
