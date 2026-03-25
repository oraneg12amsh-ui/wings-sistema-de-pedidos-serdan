from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        print("Navigating to index.html...")
        page.goto("http://localhost:8000/index.html", wait_until="commit")

        print("Waiting for intro overlay to disappear...")
        page.locator("#intro-overlay").click(force=True)
        page.wait_for_selector("#intro-overlay", state="hidden")

        print("Verifying product list renders...")
        # Check if the product list container has elements inside
        products_count = page.locator("#product-list .glass-card").count()
        print(f"Products rendered: {products_count}")
        if products_count == 0:
            print("Error: No products rendered.")
            browser.close()
            return False

        print("Adding a product to cart...")
        # Find a product that doesn't require flavor selection to simplify the test, e.g., an 'Extra' or 'Bebida'
        # Let's find the first button that is not sold out and click it. Since we might hit a modal, let's look for one that directly adds.
        # Actually, all packages/alitas open modal. Let's just click 'Papas Fritas' (id=10)
        page.locator("button[data-id='10']").first.click(force=True)

        print("Verifying cart updates...")
        cart_items_count = page.locator("#cart-list > div").count()
        print(f"Cart items rendered: {cart_items_count}")
        if cart_items_count == 0:
            print("Error: Cart item not rendered.")
            browser.close()
            return False

        print("Verification successful.")
        browser.close()
        return True

if __name__ == "__main__":
    if not verify():
        exit(1)
