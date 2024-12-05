# inventory.py
from typing import Dict

def get_inventory() -> Dict[str, float]:
    """
    Returns the inventory with items and their respective prices.
    """
    return {
        "Apples": 1.00,
        "Bananas": 0.50,
        "Carrots": 0.75,
        "Dates": 1.50,
        "Milk": 2.50,
        "Bread": 2.00,
        "Avocado": 1.25,
        "Watermelon": 3.00,
    }
