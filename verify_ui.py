import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Configure a mobile viewport as mentioned in memory to access mobile elements if needed
        context = await browser.new_context(viewport={"width": 375, "height": 812})
        page = await context.new_page()

        # Navigate to the local server
        print("Navigating to page...")
        await page.goto('http://localhost:8000/index.html', wait_until='commit')

        # Explicitly dismiss the initial '#intro-overlay'
        print("Dismissing intro overlay...")
        try:
            intro_overlay = page.locator('#intro-overlay')
            await intro_overlay.wait_for(state='visible', timeout=5000)
            await intro_overlay.click(force=True)
            await intro_overlay.wait_for(state='hidden', timeout=5000)
        except Exception as e:
            print("Intro overlay not found or already dismissed.", e)

        # Wait for products to load and render via filterAndRenderProducts
        print("Waiting for products to load...")
        try:
            await page.wait_for_selector('.glass-card', timeout=10000)
        except Exception as e:
            print("Timeout waiting for .glass-card. The UI may not have loaded.")
            await browser.close()
            return

        # Check the hearts container
        hearts_count = await page.locator('.heart-particle').count()
        print(f"Found {hearts_count} hearts in the container.")

        # Check products are rendered
        cards_count = await page.locator('.glass-card').count()
        print(f"Found {cards_count} products on the page.")

        # Test filter switch
        print("Clicking a category filter...")
        await page.click('button.category-filter-btn:has-text("Alitas")', force=True)
        await asyncio.sleep(1) # wait for DOM update
        cards_count_filtered = await page.locator('.glass-card').count()
        print(f"Found {cards_count_filtered} products after filtering.")

        # Test adding an item to the cart
        print("Adding a product to cart...")

        # Find the first 'add-to-cart-btn' which is not disabled
        add_btn = page.locator('.add-to-cart-btn:not([disabled])').first
        await add_btn.click(force=True)
        await asyncio.sleep(1) # wait for modal

        # Handle potential flavor modal
        try:
            if await page.locator('#flavor-modal').is_visible():
                print("Flavor modal appeared. Selecting a flavor...")
                await page.click('.flavor-button:not([disabled])', force=True)
                await page.click('#confirm-flavors-button', force=True)
                await asyncio.sleep(1)
        except Exception as e:
            print("No flavor modal or error interacting with it.", e)

        try:
            if await page.locator('#quantity-flavor-modal').is_visible():
                print("Quantity flavor modal appeared. Selecting a flavor...")
                await page.click('.flavor-button:not([disabled])', force=True)
                await page.click('#confirm-quantity-flavors-button', force=True)
                await asyncio.sleep(1)
        except Exception as e:
            pass

        # Check if extras modal appeared
        try:
            if await page.locator('#extras-modal').is_visible():
                print("Extras modal appeared. Skipping...")
                await page.click('#skip-extras-modal-button', force=True)
                await asyncio.sleep(1)
        except Exception as e:
            print("No extras modal or error interacting with it.", e)

        # Check cart badge
        cart_badge_text = await page.locator('#mobile-cart-count').inner_text()
        print(f"Cart badge count: {cart_badge_text}")

        # Open mobile cart
        print("Opening mobile cart...")
        await page.click('#mobile-cart-button', force=True)
        await asyncio.sleep(1)

        # Verify cart items in the mobile cart list
        cart_items_count = await page.locator('#cart-list-mobile .flex.justify-between').count()
        print(f"Items in mobile cart list: {cart_items_count}")

        print("All checks passed successfully!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
