import pytest
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