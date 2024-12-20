# Coffee Machine Project
import art
print(art.logo)
# MENU dictionary defines the types of coffee, their required ingredients, and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources available in the coffee machine
resources = {
    "water": 2000,
    "milk": 2000,
    "coffee": 250,
}


# Function to check if there are enough resources to make the selected coffee
def is_enough_items(machine_item, coffee_choice):
    if coffee_choice == 'espresso':
        if machine_item['water'] >= MENU["espresso"]["ingredients"]["water"] and machine_item['coffee'] >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        return False

    elif coffee_choice == 'latte':
        if machine_item['water'] >= MENU["latte"]["ingredients"]["water"] and machine_item['milk'] >= MENU["latte"]["ingredients"]["milk"] and machine_item['coffee'] >= MENU["latte"]["ingredients"]["coffee"]:
            return True
        return False

    elif coffee_choice == 'cappuccino':
        if machine_item['water'] >= MENU["cappuccino"]["ingredients"]["water"] and machine_item['milk'] >= MENU["cappuccino"]["ingredients"]["milk"] and machine_item['coffee'] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            return True
        return False


# Function to check if the customer has inserted enough money for the selected coffee
def is_enough_money(Q, D, N, P, coffee_choice):
    # Calculate total money inserted
    customer_money = Q * 0.25 + D * 0.10 + N * 0.05 + P * 0.01

    # Check if the customer has enough money
    if customer_money >= MENU[coffee_choice]["cost"]:
        money_to_return = customer_money - MENU[coffee_choice]["cost"]
        return True, money_to_return
    else:
        money_to_return = customer_money
        return False, money_to_return


# Function to update the machine's resources after making a coffee
def update_items_in_machine(coffee_choice, current_items):
    if coffee_choice == 'espresso':
        current_items['water'] -= MENU['espresso']['ingredients']['water']
        current_items['coffee'] -= MENU['espresso']['ingredients']['coffee']
        return current_items
    else:
        current_items['water'] -= MENU[coffee_choice]['ingredients']['water']
        current_items['milk'] -= MENU[coffee_choice]['ingredients']['milk']
        current_items['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
        return current_items


# Main logic of the coffee machine
choice = 'on'  # Variable to keep the machine running
money = 0  # Total money collected in the machine
items_in_machine = resources  # Copy of the machine's resources

while choice == 'on':

    # Update the machine's resources with current money
    items_in_machine["money"] = money

    # Prompt the user for their choice
    choice = input("What would you like? (espresso/cappuccino/latte): ")

    if choice == 'off':
        # Turn off the machine
        break

    elif choice == 'report':
        # Print the current status of the machine's resources
        print(f"water: {items_in_machine['water']} ml")
        print(f"milk: {items_in_machine['milk']} ml")
        print(f"coffee: {items_in_machine['coffee']} grams")
        print(f"money: ${items_in_machine['money']}")
        choice = 'on'

    elif choice in ['latte', 'espresso', 'cappuccino']:
        # Validate if the machine has enough resources to make the coffee
        if is_enough_items(items_in_machine, choice):
            print("Please, insert coins now")
            quarter = int(input("How many quarters? : "))
            dime = int(input("How many dimes? : "))
            nickle = int(input("How many nickles? : "))
            penny = int(input("How many pennies? : "))

            # Validate if the customer has enough money
            status, return_money = is_enough_money(quarter, dime, nickle, penny, choice)

            if status:
                # If enough money, provide the coffee and return change
                print(f"Here is your ${round(return_money, 2)} in change, collect it!")
                print(f"Here is your {choice} ☕️. Enjoy!")
                money += MENU[choice]["cost"]  # Add the cost to the machine's total money

                # Update the machine's resources
                items_in_machine = update_items_in_machine(choice, items_in_machine)
                choice = 'on'

            else:
                # If not enough money, refund the amount
                print(f"Sorry, not enough money to get you a {choice}")
                print(f"Here is your total inserted money ${round(return_money, 2)}")
                choice = 'on'

        else:
            # If not enough resources, inform the user
            print(f"Sorry, not enough items to make you a {choice}")
            choice = 'on'

    else:
        # If the user enters an invalid input
        print("Wrong input, try again")
        choice = 'on'
