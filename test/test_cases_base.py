from playwright.sync_api import Page

#Test case 1
#Valid login
def test_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert "inventory" in page.url

#Test case 2
#Invalid login
def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name" , "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    assert "Epic sadface" in page.text_content (".error-message-container")

#Test case 3
#Locators + Assertions
def test_products_visible(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    #Verify the title "Products"
    assert page.locator(".title").text_content() == "Products"

#Test case 4
#Products count and validate elements
def test_products_count(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    products = page.locator(".inventory_item")
    assert products.count() ==6

#Test case 5
#Add item to Cart
def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.click("#add-to-cart-sauce-labs-backpack")
    cart_bagde = page.locator(".shopping_cart_badge")
    assert cart_bagde.text_content() == "1"

#Test case 6
#Remove item from Cart
def test_remove_from_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#remove-sauce-labs-backpack")
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.count() == 0

#Test case 7
# Navigate to cart page
def test_go_to_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click(".shopping_cart_link")
    assert "cart" in page.url

#Test case 8
# Checkout flow
def test_start_checkout_flow(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    assert "checkout-step-one" in page.url

#Test case 9
#Complete checkout flow
def test_complete_checkout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    page.fill("#first-name", "Daniel")
    page.fill("#last-name", "Lepe")
    page.fill("#postal-code", "45599")

    page.click("#continue")
    page.click("#finish")

    assert "Thank you for your order!" in page.text_content(".complete-header")

#Test case 10
#Log out
def test_logout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    
    assert "saucedemo" in page.url




