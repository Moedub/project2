from typing import Dict

class Inventory:
    """
    Manages the inventory of grocery items and their prices.
    """

    def __init__(self) -> None:
        """
        Initializes the inventory with predefined items and their prices.
        """
        self.items: Dict[str, float] = {
            "Apples": 0.40,
            "Bananas": 0.50,
            "Carrots": 0.75,
            "Milk": 1.50,
            "Bread": 0.99,
            "Avocado": 0.39,
            "Watermelon": 2.00,
            "Grapes": 0.29,
            "Ice Cream": 0.99,
            "Beans": 0.50,
            "Sugar": 3.00,
            "Salt": 1.00,
        }

    def get_items(self) -> Dict[str, float]:
        """
        Returns the inventory items with their prices.

        Returns:
            Dict[str, float]: A dictionary of item names and their prices.
        """
        return self.items

    def get_price(self, item_name: str) -> float:
        """
        Gets the price of the given item.

        Args:
            item_name (str): The name of the item.

        Returns:
            float: The price of the item, or 0.0 if the item is not found.
        """
        return self.items.get(item_name, 0.0)
