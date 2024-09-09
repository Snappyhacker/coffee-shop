import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert customer.orders()[0].price == 5.0

def test_coffees_method():
    customer = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 4.0)
    assert len(customer.coffees()) == 2
