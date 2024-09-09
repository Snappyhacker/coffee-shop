from customer import Customer
from coffee import Coffee
from order import Order

# Example test scenario
customer1 = Customer("Alice")
coffee1 = Coffee("Latte")
order1 = Order(customer1, coffee1, 5.0)

# Output the details to verify the objects and relationships
print(f"Customer Name: {customer1.name}")
print(f"Coffee Name: {coffee1.name}")
print(f"Order Price: ${order1.price}")

# Testing relationships
print(f"Customer Orders: {customer1.orders()}")
print(f"Coffee Orders: {coffee1.orders()}")
print(f"Unique Customers for Coffee: {coffee1.customers()}")
