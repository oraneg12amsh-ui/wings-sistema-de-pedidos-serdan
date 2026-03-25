from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 375, 'height': 812})
    page.goto('http://localhost:8000')

    # Wait for the intro to disappear
    page.wait_for_selector('#intro-overlay', state='hidden', timeout=10000)

    # Click the add-to-cart button of the first product
    page.click('.add-to-cart-btn', force=True)
    time.sleep(2) # Give it time to show modal

    # We might need to select a flavor first for a package
    # Check if flavor modal is open
    if page.is_visible('#flavor-modal:not(.hidden)'):
        print("Flavor modal opened")
        # Click first available flavor
        page.locator('.flavor-button:not(.sold-out)').first.click(force=True)
        time.sleep(1)
        # Confirm flavor
        page.click('#confirm-flavors-button', force=True)
        time.sleep(2)

    # Check if extras modal is open
    if page.is_visible('#extras-modal:not(.hidden)'):
        print("Extras modal opened")
        page.click('#skip-extras-modal-button', force=True)
        time.sleep(1)

    print("Checking buttons")

    # Check for ARIA label
    aria_label = page.locator('.remove-from-cart-btn').first.get_attribute('aria-label')
    print(f"Removed button ARIA label: {aria_label}")

    aria_label_decrease = page.locator('.decrease-qty-btn').first.get_attribute('aria-label')
    print(f"Decrease button ARIA label: {aria_label_decrease}")

    aria_label_increase = page.locator('.increase-qty-btn').first.get_attribute('aria-label')
    print(f"Increase button ARIA label: {aria_label_increase}")

    aria_label_close = page.locator('#close-mobile-cart-button').first.get_attribute('aria-label')
    print(f"Close cart button ARIA label: {aria_label_close}")

    browser.close()