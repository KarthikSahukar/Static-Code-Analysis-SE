"""
FIX 1 (C0114): Added module docstring.
A simple inventory management system module.
Includes functions to add, remove, and track stock.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}



def add_item(item="default", qty=0, logs=None):
    """Adds a specified quantity of an item to the stock."""

    if logs is None:
        logs = []

    if not isinstance(item, str):
        print(f"Error: Item '{item}' is not a valid name. Skipping.")
        return

    if not isinstance(qty, int):
        print(f"Error: Quantity '{qty}' is not a valid number. Skipping.")
        return

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # FIX 5 (C0209): Converted string formatting to f-string
    logs.append(f"{datetime.now()}: Added {qty} of {item}")





def remove_item(item, qty):
    """Removes a specified quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found. Cannot remove.")



def get_qty(item):
    """Gets the current quantity of a specific item."""
    # Add a .get() for safety, defaulting to 0 if item doesn't exist
    return stock_data.get(item, 0)



def load_data(file="inventory.json"):
    """Loads stock data from a JSON file."""
    global stock_data

    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Starting with empty inventory.")
        stock_data = {}



def save_data(file="inventory.json"):
    """Saves stock data to a JSON file."""

    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)



def print_data():
    """Prints a report of all items and their quantities."""
    print("--- Items Report ---")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("--------------------")




def check_low_items(threshold=5):
    """Returns a list of items that are below the threshold."""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result







def main():
    """Main function to run the inventory system."""

    load_data()  
    add_item("apple", 10)
    add_item("banana", -2)

    add_item(123, "ten")  
    remove_item("apple", 3)
    remove_item("orange", 1)  
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    print_data()
    print('eval used')  


if __name__ == "__main__":
    main()
