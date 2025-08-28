import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page_instance = LoginPage(page)
    login_page_instance.navigate()
    return login_page_instance

class TestLogin:
    def test_smoke(self, login_page: LoginPage, page: Page):
        """Тест на успешную авторизацию с валидными данными."""
        profile_page = ProfilePage(page)
        login_page.login("standard_user", "secret_sauce")
        expect(profile_page.logo).to_be_visible()


    @pytest.mark.parametrize(
            "username, password, error_text", 
            [
                ("standard_user", "invalid_password", "Epic sadface: Username and password do not match any user in this service"),
                ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
            ]
    )
    def test_invalid_login_credentials(self, login_page: LoginPage, username, password, error_text):
        """Тест на ошибку при вводе неверного пароля."""

        login_page.login(username, password)
        expect(login_page.error_message).to_have_text(error_text)
