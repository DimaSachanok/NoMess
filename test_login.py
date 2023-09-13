from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
import pytest


@pytest.fixture
def my_fixture():
    pass


def test_login(my_fixture):
    pass


def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://109.205.183.105/")
    page.goto(
        "http://109.205.183.105:8080/realms/captain/protocol/openid-connect/auth?client_id=captain-fe&redirect_uri=http%3A%2F%2F109.205.183.105%2F&state=a759ebdf-a18f-42fc-8669-09472396830a&response_mode=fragment&response_type=code&scope=openid&nonce=bdbd4121-7fdd-4b15-8fc9-3c9dd970c6ca")
    sleep(1)
    page.get_by_label("Username or email").type("default.admin@tect.com")
    sleep(1)
    page.get_by_label("Password").type("Qwerty113!")
    sleep(1)
    page.get_by_role("button", name="Sign In").click()
    sleep(1)
    page.get_by_role("link", name="Companies").click()
    sleep(1)
    page.get_by_role("link", name="Trucks").click()
    sleep(1)
    page.get_by_role("link", name="Drivers").click()
    sleep(1)
    page.get_by_role("link", name="Trailers").click()
    sleep(1)
    page.get_by_role("link", name="Orders").click()
    sleep(1)
    page.get_by_role("link", name="Logists").click()
    sleep(1)
    page.get_by_role("link", name="Archive").click()
    sleep(1)
    # ---------------------
    context.close()
    browser.close()
# test
