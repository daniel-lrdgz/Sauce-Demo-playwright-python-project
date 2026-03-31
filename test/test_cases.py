from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from playwright.sync_api import expect
from config import BASE_URL
import allure

# Products count - Test case 1
def test_login_success(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)
    assert inventory.get_items_count() == 6

#Add products to cart - Test case 2
def test_add_to_cart(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)

    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == 1

#Remove products from cart - Test case 3
def test_remove_item_from_cart(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)

    inventory.add_item("Backpack")
    inventory.remove_first_item()
    
    assert inventory.get_cart_count() == 0

#Add 3rd product to cart - Test case 4
def test_add_3rd_to_cart(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)

    inventory.add_item("Bike Light")
    assert inventory.get_cart_count() == 1

#Wait for url - Test case 5
#To avoid flaky test use wait_for_url instead of time.sleep()
def test_wait_for_url(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)

    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    assert inventory.get_title() == "Products"

#Stable selector - Test case 6
#Impletentation to best practices in locator to avoid flaky test
def test_has_text_locators(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")

    inventory.add_item("Backpack")
    assert inventory.get_cart_count() == 1

#Check out Flow - Test case 7
def test_check_out(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)
    cart = CartPage(page)
    expect (page).to_have_url(f"{BASE_URL}/inventory.html")

    inventory.add_item("Backpack")
    assert inventory.get_cart_count() == 1
    inventory.open_cart()

    cart.start_checkout()
    checkout.fill_information("Daniel", "QA", "12345")
    checkout.finish_checkout()
    
    assert "checkout-complete" in page.url
    cart.back_to_products()
    expect (page).to_have_url(f"{BASE_URL}/inventory.html")

#Remove Item from Check out Flow - Test case 8
def test_remove_check_out_flow(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)
    cart = CartPage(page)
    expect (page).to_have_url(f"{BASE_URL}/inventory.html")

    inventory.add_item("Backpack")
    inventory.get_cart_count()
    inventory.open_cart()
    cart.remove_item("Backpack")
    assert cart.get_items_count() == 0

#Edge Case: Blocked user - Test case 9
def test_locked_user_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")

    login.validate_locked_user_error()
    
