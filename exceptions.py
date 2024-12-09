class ProductNotFoundException(Exception):
    """
    Exception raised when a product is not found in the inventory.
    """
    pass


class InsufficientStockException(Exception):
    """
    Exception raised when there is insufficient stock for a requested product.
    """
    pass
