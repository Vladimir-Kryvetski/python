from playwright.sync_api import Page, Locator

class ProfilePage:
    def __init__(self, page:Page):
        self.page = page
        self.logo = page.locator('[class="app_logo"]')