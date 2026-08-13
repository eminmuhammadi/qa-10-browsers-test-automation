class CartPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/cart.html"
        self.itemName = "Sauce Labs Backpack"
        self.itemNameElement = page.locator("div[data-test=\"inventory-item-name\"]")
        self.cartElement = page.locator("a[data-test=\"shopping-cart-link\"]")

    def click_to_cart(self):
        self.cartElement.click()