class CashRegister:
    def __init__(self, discount=0):
        # Initialize the private variable for discount
        self._discount = 0
        self.discount = discount
        
        # Initialize total and arrays
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Check if the value is an integer and strictly between 0 and 100
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        # Add item to the items list
        self.items.append(item)
        
        self.total += price
        
        # Add dictionary to previous_transactions
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Apply discount as a percentage off the total
            self.total -= (self.total * (self.discount / 100))

    def void_last_transaction(self):

        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        
        last_transaction = self.previous_transactions.pop()
        self.items.pop()
        self.total -= last_transaction["price"]