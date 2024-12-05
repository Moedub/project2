# gui.py
import tkinter as tk
from tkinter import messagebox
from inventory import get_inventory
from transaction_logger import log_transaction
from typing import List, Dict

class GroceryApp:
    def __init__(self, root: tk.Tk):
        """
        Initialize the grocery shopping app with GUI components.
        """
        self.root = root
        self.root.title("Grocery Shopping Cart")
        self.inventory = get_inventory()
        self.cart: List[str] = []

        # Inventory section
        self.inventory_label = tk.Label(root, text="Inventory")
        self.inventory_label.grid(row=0, column=0)
        self.inventory_listbox = tk.Listbox(root, height=10, width=30)
        self.inventory_listbox.grid(row=1, column=0)
        self.populate_inventory()

        # Cart section
        self.cart_label = tk.Label(root, text="Cart")
        self.cart_label.grid(row=0, column=1)
        self.cart_listbox = tk.Listbox(root, height=10, width=30)
        self.cart_listbox.grid(row=1, column=1)

        # Buttons
        self.add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=2, column=0)

        self.remove_from_cart_button = tk.Button(root, text="Remove from Cart", command=self.remove_from_cart)
        self.remove_from_cart_button.grid(row=2, column=1)

        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=3, column=0, columnspan=2)

    def populate_inventory(self) -> None:
        """
        Populate the inventory listbox with items and their prices.
        """
        self.inventory_listbox.delete(0, tk.END)
        for item, price in self.inventory.items():
            self.inventory_listbox.insert(tk.END, f"{item} - ${price:.2f}")

    def populate_cart(self) -> None:
        """
        Populate the cart listbox with items.
        """
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart:
            self.cart_listbox.insert(tk.END, f"{item} - ${self.inventory[item]:.2f}")

    def add_to_cart(self) -> None:
        """
        Add the selected item from inventory to the cart.
        """
        selection = self.inventory_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select an item to add to the cart.")
            return

        selected_item = list(self.inventory.keys())[selection[0]]
        self.cart.append(selected_item)
        self.populate_cart()

    def remove_from_cart(self) -> None:
        """
        Remove the selected item from the cart.
        """
        selection = self.cart_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select an item to remove from the cart.")
            return

        selected_item = self.cart[selection[0]]
        self.cart.remove(selected_item)
        self.populate_cart()

    def checkout(self) -> None:
        """
        Display the items in the cart and the total price in a message box.
        """
        if not self.cart:
            messagebox.showinfo("Cart", "Your cart is empty.")
            return

        total_price = sum(self.inventory[item] for item in self.cart)
        receipt = "\n".join([f"{item} - ${self.inventory[item]:.2f}" for item in self.cart])
        receipt += f"\n\nTotal: ${total_price:.2f}"

        messagebox.showinfo("Checkout", f"Items in your cart:\n{receipt}")
        log_transaction(f"Checked out items:\n{receipt}")
        self.cart = []
        self.populate_cart()
