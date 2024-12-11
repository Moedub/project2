class Inventory:
    """
    Manages the inventory of grocery items and their prices.
    """

    def __init__(self) -> None:
        self.items = {
            # Fruits
            "Apples": 0.40,
            "Bananas": 0.50,
            "Grapes": 0.29,
            "Watermelon": 2.00,
            "Avocado": 0.39,
            "Oranges": 0.45,
            "Strawberries": 1.20,
            "Pineapple": 1.50,
            "Blueberries": 2.50,

            # Vegetables
            "Carrots": 0.75,
            "Broccoli": 1.10,
            "Potatoes": 0.70,
            "Tomatoes": 0.60,
            "Lettuce": 0.80,
            "Onions": 0.40,
            "Spinach": 1.00,
            "Peppers": 1.30,

            # Dairy
            "Milk": 1.50,
            "Cheese": 2.50,
            "Yogurt": 1.20,
            "Butter": 1.80,
            "Cream": 1.40,

            # Bakery
            "Bread": 0.99,
            "Bagels": 1.50,
            "Croissants": 2.00,
            "Muffins": 1.75,

            # Beverages
            "Water": 1.00,
            "Juice": 2.50,
            "Soda": 2.00,
            "Coffee": 3.00,
            "Tea": 2.00,

            # Snacks
            "Cookies": 1.50,
            "Chips": 1.20,
            "Candy": 1.00,
            "Chocolate": 2.00,
            "Popcorn": 1.00,

            # Pantry Items
            "Rice": 3.00,
            "Beans": 0.50,
            "Flour": 1.50,
            "Sugar": 3.00,
            "Salt": 1.00,
            "Pasta": 2.00,
            "Oil": 5.00,

            # Frozen Foods
            "Ice Cream": 0.99,
            "Frozen Pizza": 4.00,
            "Frozen Vegetables": 2.50,
            "Frozen Fries": 2.00,

            # Meat & Fish
            "Chicken Breast": 5.50,
            "Beef": 7.00,
            "Fish": 6.00,
            "Shrimp": 8.00,
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
