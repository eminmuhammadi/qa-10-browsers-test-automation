import time

import pytest

from pages.inventory import InventoryPage
from pages.login import LoginPage


# Har viewers - https://toolbox.googleapps.com/apps/har_analyzer/
# Trace viewers - https://trace.playwright.dev/
# py -m pytest -v --browser chromium --headed -q --tracing=on --video=on --html=reports/report.html --tags login --slowmo 2000
# py -m pytest -v --browser firefox --headed -q --tracing=on --video=on --html=reports/report.html
# py -m pytest -v --browser webkit --headed -q --tracing=on --video=on --html=reports/report.html
# Docs: https://playwright.dev/python/docs/test-runners
@pytest.fixture(scope="session")
def context(browser, request):
    TC = f"{request.node.name}-{time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())}"

    context = browser.new_context(
        # viewport={"width": 844, "height": 1080},
        is_mobile=False,
        has_touch=False,
        locale="en-US",
        java_script_enabled=True,
        record_video_dir=f"reports/artifact_{TC}",
        record_har_path=f"reports/artifact_{TC}/network.har",
        record_har_mode="full",
    )

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    context.tracing.stop(path=f"reports/artifact_{TC}/trace.zip")
    context.close()


@pytest.fixture(scope="session")
def page(context):
    # https://playwright.dev/python/docs/api/class-page
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def inventory_page(page):
    loginPage = LoginPage(page)
    loginPage.visit()
    loginPage.login("standard_user", "secret_sauce")

    return InventoryPage(page)
