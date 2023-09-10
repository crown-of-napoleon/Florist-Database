import pytest
from app import run as app_run
from EmployeeApp import run as employee_run
from InventoryApp import run as inventory_run
from SalesApp import run as sales_run

# Mocking the print function to avoid console outputs during testing
@pytest.fixture(autouse=True)
def no_prints(monkeypatch):
    monkeypatch.setattr("builtins.print", lambda x: None)

def test_customer_run():
    # Test the customer app's run function
    assert customer_run() is None

def test_employee_run():
    # Test the employee app's run function
    assert employee_run() is None

def test_inventory_run():
    # Test the inventory app's run function
    assert inventory_run() is None

def test_sales_run():
    # Test the sales app's run function
    assert sales_run() is None

# Additional tests can be added below

