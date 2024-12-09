class Inventory:
    """
    Manages the inventory of grocery items and their prices.
    """

    def __init__(self):
        self.items = {
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

    def get_items(self) -> dict:
        """
        Returns the inventory items with their prices.
        """
        return self.items

    def get_price(self, item_name: str) -> float:
        """
        Gets the price of the given item.

        Args:
            item_name (str): The name of the item.

        Returns:
            float: The price of the item.
        """
        return self.items.get(item_name, 0.0)
