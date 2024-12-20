
# Coffee Machine Project

## Description
This Python project simulates a coffee machine that can serve three types of coffee: Espresso, Latte, and Cappuccino. The user interacts with the coffee machine through a terminal-based interface, selects a coffee, and inserts coins. The machine validates if the customer has enough money and whether the machine has enough resources to make the coffee.

## Features
- Users can choose from 3 coffee options: **Espresso**, **Latte**, **Cappuccino**.
- The machine tracks the resources (water, milk, coffee) and informs the user if there aren't enough resources.
- Users are asked to insert coins (quarters, dimes, nickels, and pennies) for payment.
- The machine returns change if the customer inserts more than required.
- Users can check the available resources and money in the machine through the "report" option.
- The program stops when the user types "off".

## Requirements
- Python 3.x

## How to Use
1. Clone the repository to your local machine.
2. Navigate to the project folder using the terminal.
3. Run the program with the following command:
   ```bash
   python coffee_machine.py
   ```
4. When prompted, choose a coffee by typing **espresso**, **latte**, or **cappuccino**.
5. Insert coins when asked (quarters, dimes, nickels, pennies).
6. The machine will either make the coffee and return change or notify you of insufficient resources or funds.
7. Type **report** to see the current machine status (remaining resources and money).
8. Type **off** to turn off the machine.

## File Structure
- `coffee_machine.py` - The main program containing the logic for the coffee machine.
- `art.py` - Contains ASCII art or logo that is displayed when the program starts.
- `.gitignore` - Specifies files and directories (like `.idea/` and `__pycache__/`) that should be ignored by Git.

## Example Interaction

```plaintext
What would you like? (espresso/cappuccino/latte): espresso
Please, insert coins now
How many quarters? : 2
How many dimes? : 1
How many nickels? : 1
How many pennies? : 1
Here is your $0.16 in change, collect it!
Here is your espresso ☕️. Enjoy!
```

## Contribution
Feel free to fork the project, make improvements, or report bugs. Pull requests are welcome!

## License
This project is open-source and available under the MIT License.

## Author
This project was created by Nitish Raj.
