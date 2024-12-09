from typing import List, Dict

class Cart:
    """
    A class to represent a shopping cart.

    Attributes:
        items (List[Dict[str, int]]): A list of items in the cart, each represented as a dictionary with item name and quantity.
    """

    def __init__(self) -> None:
        """
        Initializes an empty shopping cart.
        """
        self.items: List[Dict[str, int]] = []

    def add_item(self, item: str, quantity: int) -> None:
        """
        Adds an item to the cart.

        Args:
            item (str): Name of the item.
            quantity (int): Quantity of the item to add.
        """
        self.items.append({"item": item, "quantity": quantity})

    def remove_item(self, item: str) -> None:
        """
        Removes an item from the cart.

        Args:
            item (str): Name of the item to remove.
        """
        self.items = [i for i in self.items if i["item"] != item]

    def view_cart(self) -> List[Dict[str, int]]:
        """
        Returns the list of items in the cart.

        Returns:
            List[Dict[str, int]]: The items currently in the cart.
        """
        return self.items
