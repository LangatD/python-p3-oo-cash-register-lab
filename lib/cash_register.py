class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the CashRegister with an optional discount.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """
        Add an item to the register.
        """
        self.total += price * quantity
        self.last_transaction = price * quantity
        # Add the item and its quantity to the list
        self.items.extend([title] * quantity)

    def apply_discount(self):
        """
        Apply the discount to the total, if applicable.
        """
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Void the last transaction and update the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0
