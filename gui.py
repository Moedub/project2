import tkinter as tk
from tkinter import ttk
from inventory import Inventory
from transaction_logger import TransactionLogger


class GroceryStoreApp:
    """
    A modernized GUI for a grocery store app using ttk.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Mohamed\'s Grocery Store")
        self.root.geometry("500x400")

        # Apply ttk theme
        ttk.Style().theme_use("clam")

        # Initialize inventory and cart
        self.inventory = Inventory()
        self.transaction_logger = TransactionLogger()
        self.cart = {}

        # Create main frames
        self.inventory_frame = ttk.LabelFrame(self.root, text="Inventory", padding=(10, 10))
        self.cart_frame = ttk.LabelFrame(self.root, text="Cart", padding=(10, 10))
        self.inventory_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.cart_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Inventory section
        self.inventory_listbox = tk.Listbox(self.inventory_frame, height=10, width=25)
        self.populate_inventory()
        self.inventory_listbox.grid(row=0, column=0, padx=5, pady=5)

        self.quantity_label = ttk.Label(self.inventory_frame, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, sticky="w", padx=5)

        self.quantity_entry = ttk.Entry(self.inventory_frame, width=10)
        self.quantity_entry.grid(row=1, column=0, sticky="e", padx=5)

        self.add_to_cart_button = ttk.Button(
            self.inventory_frame, text="Add to Cart", command=self.add_to_cart
        )
        self.add_to_cart_button.grid(row=2, column=0, pady=10)

        # Cart section
        self.cart_listbox = tk.Listbox(self.cart_frame, height=10, width=25)
        self.cart_listbox.grid(row=0, column=0, padx=5, pady=5)

        self.remove_from_cart_button = ttk.Button(
            self.cart_frame, text="Remove from Cart", command=self.remove_from_cart
        )
        self.remove_from_cart_button.grid(row=1, column=0, pady=5)

        self.checkout_button = ttk.Button(
            self.cart_frame, text="Checkout", command=self.checkout
        )
        self.checkout_button.grid(row=2, column=0, pady=10)

        # Status Bar
        self.status_label = ttk.Label(self.root, text="Welcome to the Grocery Store!", anchor="center")
        self.status_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

    def populate_inventory(self):
        """Populate the inventory listbox with items."""
        for item, price in self.inventory.get_items().items():
            self.inventory_listbox.insert(tk.END, f"{item} - ${price:.2f}")

    def add_to_cart(self):
        """Add the selected item to the cart."""
        try:
            # Get the selected inventory item
            selected_item_index = self.inventory_listbox.curselection()

            # Check if no inventory item is selected
            if not selected_item_index:
                self.status_label.config(text="Please select an inventory.")
                return

            selected_item = self.inventory_listbox.get(selected_item_index).split(" - ")[0]

            # Get the quantity entered
            quantity = self.quantity_entry.get().strip()

            # Validate quantity input
            if not quantity.isdigit() or int(quantity) <= 0:
                self.status_label.config(text="Please enter a valid quantity.")
                return

            quantity = int(quantity)

            # Add the item to the cart
            if selected_item in self.cart:
                self.cart[selected_item] += quantity
            else:
                self.cart[selected_item] = quantity

            self.update_cart_display()
            self.status_label.config(text=f"Added {quantity} x {selected_item} to cart.")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

    def remove_from_cart(self):
        """Remove the selected item from the cart."""
        if not self.cart:  # Check if the cart is empty
            self.status_label.config(text="Nothing in cart.")
            return

        try:
            # Get the selected cart item
            selected_item_index = self.cart_listbox.curselection()

            # Check if no cart item is selected
            if not selected_item_index:
                self.status_label.config(text="Please choose the item you want to remove.")
                return

            selected_item = self.cart_listbox.get(selected_item_index).split(" x ")[0]

            # Remove the item from the cart
            del self.cart[selected_item]

            self.update_cart_display()
            self.status_label.config(text=f"Removed {selected_item} from cart.")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

    def update_cart_display(self):
        """Update the cart listbox to show the current items."""
        self.cart_listbox.delete(0, tk.END)
        for item, quantity in self.cart.items():
            self.cart_listbox.insert(tk.END, f"{item} x {quantity}")

    def checkout(self):
        """Handle the checkout process."""
        if not self.cart:
            self.status_label.config(text="Cart is empty!")
            return

        total_cost = sum(
            self.inventory.get_price(item) * quantity for item, quantity in self.cart.items()
        )
        self.transaction_logger.log_transaction(self.cart, total_cost)
        self.status_label.config(text=f"Checked out! Total: ${total_cost:.2f}")
        self.cart.clear()
        self.update_cart_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryStoreApp(root)
    root.mainloop()
