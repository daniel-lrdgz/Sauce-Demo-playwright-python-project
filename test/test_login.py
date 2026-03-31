import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_success(page):
    login = LoginPage (page)
    inventory = InventoryPage(page)

    login.navigate()
    login.login ("standard_user","secret_sauce")

    assert "inventory" in page.url
    assert inventory.get_title() == "Products"

def test_login_invalid(page):
    login = LoginPage(page)

    login.navigate()
    login.login("standard_user", "wrong_password")

    assert "Epic sadface" in login.get_error()
