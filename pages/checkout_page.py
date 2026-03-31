
from playwright.sync_api import Page
import allure

class CheckoutPage():

    def __init__(self, page: Page):
        self.page = page
        self.title = ".title"
        self.items = ".checkout_item"

    def get_title(self):
        return self.page.locator(self.title).text_content()
    
    @allure.step("Get checkout item count")
    def get_items_count(self):
        return self.page.locator(self.items).count()
    
    @allure.step("Remove item {name} from checkout")
    def remove_item(self, name):
        return self.page.locator(f".cart_item:has-text('{name}')").click()
    
    @allure.step("Return to shopping")
    def return_to_shopping (self):
        return self.page.click("#back-to-products")

    @allure.step("Fill {first} information to checkout")
    def fill_information(self, first, last, zip):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip)
        self.page.click("#continue")

    @allure.step("Complete checkout")
    def finish_checkout(self):
        self.page.click("#finish")