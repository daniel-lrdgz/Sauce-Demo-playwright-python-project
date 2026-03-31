from playwright.sync_api import Page
from config import BASE_URL
import allure

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = ".error-message-container"

    def navigate(self):
        self.page.goto ("/")

    @allure.step("Login {username} user")
    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    @allure.step("Get error login")
    def get_error(self):
        return self.page.locator(self.error_message).text_content()
    
    @allure.step("Get login error message")
    def get_error_message(self):
        return self.page.locator(".error-message-container").text_content()
    
    @allure.step("Validate locked out user error")
    def validate_locked_user_error(self):
        message = self.get_error_message()
        assert "locked out" in message, f"Unexpected error message: {message}"