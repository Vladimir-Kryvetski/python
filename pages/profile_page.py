from playwright.sync_api import Page

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator('.app_logo')