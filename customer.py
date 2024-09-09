class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) > 15:
            raise ValueError("Name must be a string of 1 to 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid Coffee instance.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid Coffee instance.")
        customer_spending = {}
        for order in coffee._orders:
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)
