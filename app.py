from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create new page
    page = browser.new_page()
    # Visit playwright website
    page.goto("https://playwright.dev/python")
    # Locator
    docs_link = page.get_by_role('link', name="Get Started")
    docs_link.click()

    browser.close()
