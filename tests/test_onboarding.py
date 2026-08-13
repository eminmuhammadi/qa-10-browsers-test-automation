import pytest

from pages.inventory import InventoryPage
from pages.login import LoginPage
from pages.cart import CartPage
from playwright.sync_api import expect

"""
-- Steps to reproduce
1. Go to https://www.saucedemo.com/ this URL
2. Click to #user-name
3. Fill #user-name with value "standard_user"
4. Click to #password
5. Fill #password with value "secret_sauce"
6. Click to #login-button

-- Expected result (Assertion)
Expect span[data-test="title"] contains text "Products"
"""


# https://playwright.dev/python/docs/api/class-locator
@pytest.mark.tags("login")
def test_verify_that_standard_user_can_login(page):
    page.goto("https://www.saucedemo.com/")
    # Username
    page.locator("#user-name").click()
    page.locator("#user-name").fill("standard_user")
    # Password
    page.locator("#password").click()
    page.locator("#password").fill("secret_sauce")
    # Button
    page.locator("#login-button").click()
    # Assertion
    expect(page.locator("span[data-test='title']")).to_contain_text("Products")


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
    ],
)
@pytest.mark.tags("login_pom")
def test_verify_that_users_can_login_with_pom(page, username, password):
    loginPage = LoginPage(page)
    loginPage.visit()
    loginPage.login(username, password)

    inventoryPage = InventoryPage(page)
    expect(inventoryPage.titleElement).to_contain_text(inventoryPage.title)


@pytest.mark.tags("login_precondition")
def test_verify_that_users_can_see_inventory_page(inventory_page):
    expect(inventory_page.titleElement).to_contain_text(inventory_page.title)


@pytest.mark.tags("add_to_cart")
def test_verify_that_users_can_add_product_to_cart(inventory_page):
    inventory_page.add_to_cart()

    cartPage = CartPage(inventory_page.page)
    cartPage.click_to_cart()

    expect(cartPage.itemNameElement).to_contain_text(cartPage.itemName)
