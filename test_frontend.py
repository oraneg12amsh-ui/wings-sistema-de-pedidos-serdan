from playwright.sync_api import sync_playwright

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport configuration as per instructions
        context = browser.new_context(
            viewport={"width": 375, "height": 812},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        )
        page = context.new_page()

        print("Navigating to local server...")
        page.goto("http://localhost:8000")

        print("Waiting for intro overlay...")
        # Dismiss intro overlay
        page.wait_for_selector("#intro-overlay", state="visible", timeout=5000)
        page.click("#intro-overlay", force=True)
        page.wait_for_selector("#intro-overlay", state="hidden", timeout=5000)

        print("Adding product to cart...")
        # Find the first available product to add
        page.wait_for_selector(".add-to-cart-btn:not([disabled])", timeout=5000)
        buttons = page.locator(".add-to-cart-btn:not([disabled])")

        # Click the first enabled button
        first_btn = buttons.first
        first_btn.click(force=True)

        print("Handling flavor/qty modal if it appears...")
        try:
            # Try to handle flavor modal if it pops up
            flavor_modal = page.locator("#flavor-modal:visible, #quantity-flavor-modal:visible").first
            if flavor_modal.is_visible(timeout=2000):
                # Select a flavor if possible
                flavor_btn = flavor_modal.locator(".flavor-button:not(.sold-out)").first
                if flavor_btn.is_visible():
                    flavor_btn.click(force=True)

                # Confirm modal
                confirm_btn = flavor_modal.locator("button:has-text('Confirmar'), button:has-text('Añadir')").first
                confirm_btn.click(force=True)
        except Exception as e:
            print(f"No flavor modal or error handling it: {e}")

        try:
            # Try to handle extras modal if it pops up
            extras_modal = page.locator("#extras-modal:visible")
            if extras_modal.is_visible(timeout=2000):
                # Skip extras
                skip_btn = page.locator("#skip-extras-modal-button")
                skip_btn.click(force=True)
        except Exception as e:
            print(f"No extras modal or error handling it: {e}")

        print("Verifying cart count...")
        # Check if mobile cart count updated
        page.wait_for_selector("#mobile-cart-count", state="visible", timeout=5000)
        count_text = page.locator("#mobile-cart-count").inner_text()

        print(f"Cart count is: {count_text}")
        assert int(count_text) > 0, f"Expected cart count > 0, got {count_text}"

        print("Frontend verification successful!")
        browser.close()

if __name__ == "__main__":
    test_frontend()
