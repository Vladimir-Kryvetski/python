from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def smoke_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # cоздаем экземпляр класса LoginPage и ProfilePage
        login_page = LoginPage(page)
        profile_page = ProfilePage(page)

        # Шаг №1 - Открыть страницу авторизации
        login_page.navigate()

        # Шаг №2 - Отправить форму с валиднными личными данными
        login_page.login("standard_user", "secret_sauce")

        # №3 - Проверить переход на страницу профиля
        expect(profile_page.logo).to_be_visible()
        print('Успешная авторизация с валидными данными')

        browser.close()

def invalid_password ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

         # Шаг №1 - Открыть страницу авторизации
        login_page.navigate()

        # Шаг №2 - Отправить форму с  невалиднными личными данными
        login_page.login("standard_user", "invalid_password")

        # №3 - Проверить наличие ошибки
        expect(login_page.password_error).to_have_text('Epic sadface: Username and password do not match any user in this service')
        print('Показывается текст ошибки')

        browser.close()

if __name__ == '__main__':
    smoke_test(), invalid_password()
