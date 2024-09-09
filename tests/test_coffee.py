import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    assert coffee.num_orders() == 1

def test_average_price():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 7.0)
    assert coffee.average_price() == 6.0
