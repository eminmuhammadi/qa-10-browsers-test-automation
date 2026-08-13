class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.usernameElement = page.locator("#user-name")
        self.passwordElement = page.locator("#password")
        self.loginButtonElement = page.locator("#login-button")

    def visit(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.usernameElement.click()
        self.usernameElement.fill(username)
        self.passwordElement.click()
        self.passwordElement.fill(password)
        self.loginButtonElement.click()