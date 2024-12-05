# transaction_logger.py
def log_transaction(transaction: str) -> None:
    """
    Logs the transaction to a file.
    """
    with open("transactions.log", "a") as log_file:
        log_file.write(transaction + "\n")
