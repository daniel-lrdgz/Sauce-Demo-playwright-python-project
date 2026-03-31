from playwright.sync_api import Page
import allure

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = ".title"
        self.items = ".inventory_item"

    @allure.step("Get title")
    def get_title(self):
        return self.page.locator(self.title).text_content()
    
    #Main page inventory
    @allure.step("Get items count")
    def get_items_count(self):
        return self.page.locator(self.items).count()
    
    @allure.step("Add first item to cart")
    def add_first_item_to_cart(self):
        return self.page.locator(".inventory_item button").first.click()
    
    @allure.step("Remove first item from cart")
    def remove_first_item(self):
        return self.page.locator(".inventory_item button").first.click()
    
    @allure.step("Add {name} to cart")
    def add_item(self, name):
        return self.page.locator(f".inventory_item:has-text('{name}') button").click()

    @allure.step("Open cart")
    def open_cart(self):
        return self.page.locator(".shopping_cart_badge").click()

    #Icon cart count
    @allure.step("Get cart count")
    def get_cart_count(self):
        badge = self.page.locator(".shopping_cart_badge")
        
        if badge.count() == 0:
            return 0
        
        return int(badge.text_content())
    
