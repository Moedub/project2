class TransactionLogger:
    """
    Handles logging of transactions to a file.
    """
    def __init__(self):
        self.log_file = "transactions.log"

    def log_transaction(self, cart: dict, total_cost: float):
        """
        Logs the details of a transaction.

        Args:
            cart (dict): The items in the cart and their quantities.
            total_cost (float): The total cost of the transaction.
        """
        with open(self.log_file, "a") as file:
            file.write("Transaction Details:\n")
            for item, quantity in cart.items():
                file.write(f"{item} x {quantity}\n")
            file.write(f"Total Cost: ${total_cost:.2f}\n")
            file.write("-" * 20 + "\n")
