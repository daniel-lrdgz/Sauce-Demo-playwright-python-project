from playwright.sync_api import Page
import allure

class CartPage:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Remove {name} from Cart")
    def remove_item(self, name):
        self.page.locator(f".cart_item:has-text('{name}') button").click()

    @allure.step("Start checkout")
    def start_checkout(self):
        self.page.click("#checkout")

    @allure.step("Return to products")
    def back_to_products(self):
        self.page.click("#back-to-products")

    @allure.step("Get cart items count")
    def get_items_count(self):
        return self.page.locator(".cart_item").count()