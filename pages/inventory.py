class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"
        self.title = "Products"
        self.titleElement = page.locator("span[data-test='title']")
        self.addToCartElement = page.locator("#add-to-cart-sauce-labs-backpack")

    def add_to_cart(self):
        self.addToCartElement.click()