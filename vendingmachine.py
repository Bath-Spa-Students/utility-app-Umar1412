class VendingMachine:

# Creating 2 dictionaries named drinks menu and snacks menu
# They contain the item code, name of the item and the price

    drinks_menu = {
        "Um1": {"name": "Water", "price": 1},
        "Um2": {"name": "Red Bull", "price": 9},
        "Um3": {"name": "Pepsi", "price": 3},
        "Um4": {"name": "Lipton ice tea", "price": 4},
        "Um6": {"name": "Mountain Dew", "price": 3},
        "Um7": {"name": "Strawberry Milk", "price": 2},
        "Um8": {"name": "Chocolate Milk", "price": 2}
    }

    snacks_menu = {
        "As1": {"name": "Cheetos", "price": 4},
        "As2": {"name": "Kit Kat", "price": 2},
        "As3": {"name": "Kinder Bueno", "price": 3},
        "As4": {"name": "Lays Ketchup", "price": 1},
        "As5": {"name": "Oman Chips", "price": 1},
        "As6": {"name": "Pringles BBQ", "price": 4},
        "As7": {"name": "Maltesers", "price": 4}, 
        "As8": {"name": "Hershey's cookies and creme", "price": 3}
    }

# Number of stock avaliable to the user to purchase for both menus

    drinks_stock = {item: 8 for item in drinks_menu}
    snacks_stock = {item: 8 for item in snacks_menu}

# Total cost and user balance set to 0.0

    total_cost = 0.0
    user_balance = 0.0

  # A function to display a logo

    def display_logo(logo):
        print(logo)

   # A function to display the menu to the user

    def display_menu(menu, menu_name, logo=None):
        if logo:
            VendingMachine.display_logo(logo)

        for item, details in menu.items():
            print(f"{item}: {details['name']} - AED {details['price']:.2f}")

  # A function that takes user input for quantity and shows different statements based on the users selection

    def stock_input(item, stock_menu):
        while True:
            try:
                stock = int(input(f"How many {item}s would you like to buy today? :) (Available: {stock_menu[item]}): "))
                if 1 <= stock <= stock_menu[item]:
                    return stock
                else:
                    print(f"That number of items is not available. Enter a number 1 to {stock_menu[item]}.")
            except ValueError:
                print("Error. Please enter a valid number.")

   # A function for the user to choose items and adjust the overall cost
   # Gives the user a statement asking the user to enter item code or end 

    def item_selection(menu, stock_menu, logo=None):
        selection = input("\nEnter item code or click the done button to end (TYPE IN 'done') : ").capitalize()

        while selection != 'Done':
            if selection in menu:
                if menu == VendingMachine.snacks_menu:

                    # Display snacks logo

                    logo_snacks = """
                     ____  _   _    _    ____ _  ______  
                    / ___|| \ | |  / \  / ___| |/ / ___| 
                    \___ \|  \| | / _ \| |   | ' /\___ \ 
                     ___) | |\  |/ ___ \ |___| . \ ___) |
                    |____/|_| \_/_/   \_\____|_|\_\____/  
                    """
                    VendingMachine.display_logo(logo_snacks)

                elif menu == VendingMachine.drinks_menu:

                    # Display drinks logo

                    logo_drinks = """
                     ____  ____  ___ _   _ _  ______  
                    |  _ \|  _ \|_ _| \ | | |/ / ___| 
                    | | | | |_) || ||  \| | ' /\___ \ 
                    | |_| |  _ < | || |\  | . \ ___) |
                    |____/|_| \_\___|_| \_|_|\_\____/  
                    """
                    VendingMachine.display_logo(logo_drinks)

                stock = VendingMachine.stock_input(selection, stock_menu)
                VendingMachine.total_cost += menu[selection]['price'] * stock
                stock_menu[selection] -= stock
                print(f"\nAdded {stock} {menu[selection]['name']}(s) to your selection. Your total cost is: AED {VendingMachine.total_cost:.2f}")
            else:
                print("Invalid code. Please enter a valid item code.")

            selection = input("\nEnter item code or click the done button to end (TYPE IN 'done') : ").capitalize()

   # A function that asks the users input for how much money they would like to use.
   # First thing the user would see and interact with

    def users_money():
        while True:
            try:
                money_input = float(input("Insert the amount you would like to use (AED): "))
                if money_input >= 0:
                    VendingMachine.user_balance = money_input
                    break
                else:
                    print("Please enter a valid amount.")
            except ValueError:
                print("Error. Please enter a valid amount.")

# A function that starts the vending machine
    def start_purchase():

        # Display vending machine logo

        logo_vending_machine = """
         _   _______  _____  _____  _______  __  ______  _______ _______  ______
        | | / / __/ |/ / _ \/  _/ |/ / ___/ /  |/  / _ |/ ___/ // /  _/ |/ / __/
        | |/ / _//    / // // //    / (_ / / /|_/ / __ / /__/ _  // //    / _/  
        |___/___/_/|_/____/___/_/|_/\___/ /_/  /_/_/ |_\___/_//_/___/_/|_/___/   
        """
        VendingMachine.display_logo(logo_vending_machine)

# Displays snacks menu along with its logo

        logo_snacks = """
         ____  _   _    _    ____ _  ______  
        / ___|| \ | |  / \  / ___| |/ / ___| 
        \___ \|  \| | / _ \| |   | ' /\___ \ 
         ___) | |\  |/ ___ \ |___| . \ ___) |
        |____/|_| \_/_/   \_\____|_|\_\____/  
        """
        VendingMachine.display_menu(VendingMachine.snacks_menu, "Snacks", logo_snacks)
        VendingMachine.item_selection(VendingMachine.snacks_menu, VendingMachine.snacks_stock, logo_snacks)

# Displays drinks menu along with its logo

        logo_drinks = """
         ____  ____  ___ _   _ _  ______  
        |  _ \|  _ \|_ _| \ | | |/ / ___| 
        | | | | |_) || ||  \| | ' /\___ \ 
        | |_| |  _ < | || |\  | . \ ___) |
        |____/|_| \_\___|_| \_|_|\_\____/  
        """
        VendingMachine.display_menu(VendingMachine.drinks_menu, "Drinks", logo_drinks)
        VendingMachine.item_selection(VendingMachine.drinks_menu, VendingMachine.drinks_stock, logo_drinks)

# Completes the purchase

        VendingMachine.checkout()

 # A checkout function that gives the user comments about their purchase.

    def checkout():
        print("\nThank you for using the Vending Machine :) hope you had a great experience!")

        if VendingMachine.total_cost > VendingMachine.user_balance:
            print(f"Insufficient funds. Your total cost is: AED {VendingMachine.total_cost:.2f}")
        else:
            change = VendingMachine.user_balance - VendingMachine.total_cost
            print(f"The total amount is: AED {VendingMachine.total_cost:.2f}")
            print(f"Please collect your change: AED {change:.2f}")

# Users input for the amount of money they would like to use
# Starting the vending machine

VendingMachine.users_money()
VendingMachine.start_purchase()