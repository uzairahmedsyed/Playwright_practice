
# from playwright.sync_api import Page

# def test_open_google(page: Page):
#     page.goto("https://www.google.com")
#     print("Google khul gaya!")


from playwright.sync_api import Page

def test_google_search(page: Page):
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)