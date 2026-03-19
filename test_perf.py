import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Use mobile viewport for better testing of mobile cart functionality
        context = await browser.new_context(viewport={"width": 375, "height": 812})
        page = await context.new_page()

        await page.goto("http://localhost:8000/index.html")

        print("Testing initial render...")

        # Click the intro overlay to bypass it (based on memory guidelines)
        await page.click('#intro-overlay', force=True)
        await page.wait_for_timeout(1000)

        # Verify products rendered
        products_rendered = await page.locator('.glass-card').count()
        print(f"Products rendered: {products_rendered}")
        assert products_rendered > 0, "No products were rendered!"

        # Find first product that is NOT sold out to add to cart
        # We need an available product to test the cart
        add_btn = page.locator('.add-to-cart-btn:not([disabled])').first
        await add_btn.wait_for(state="visible")
        print("Clicking add to cart for first available product...")
        await add_btn.click(force=True)

        await page.wait_for_timeout(500)

        # Check for flavor modal if the product requires it
        flavor_modal = page.locator('#flavor-modal')
        if await flavor_modal.is_visible():
            print("Flavor modal appeared, selecting flavor...")
            flavor_btn = flavor_modal.locator('.flavor-button:not([disabled])').first
            await flavor_btn.click(force=True)
            await page.wait_for_timeout(500)
            await page.locator('#confirm-flavors-button').click(force=True)
        else:
            qty_flavor_modal = page.locator('#quantity-flavor-modal')
            if await qty_flavor_modal.is_visible():
                print("Quantity flavor modal appeared, selecting flavor...")
                flavor_btn = qty_flavor_modal.locator('.flavor-button:not([disabled])').first
                await flavor_btn.click(force=True)
                await page.wait_for_timeout(500)
                await page.locator('#confirm-quantity-flavors-button').click(force=True)

        await page.wait_for_timeout(500)

        # Check for extras modal
        extras_modal = page.locator('#extras-modal')
        if await extras_modal.is_visible():
            print("Extras modal appeared, skipping...")
            await page.locator('#skip-extras-modal-button').click(force=True)

        await page.wait_for_timeout(500)

        # Open mobile cart to verify renderList worked correctly
        print("Opening mobile cart...")
        await page.locator('#mobile-cart-button').click(force=True)
        await page.wait_for_timeout(1000)

        cart_items_rendered = await page.locator('#cart-list-mobile .flex.justify-between').count()
        print(f"Cart items rendered: {cart_items_rendered}")

        if cart_items_rendered > 0:
             print("Test passed: DOM modifications successfully rendered elements")
        else:
            print("Test failed: No items found in cart, rendering might be broken.")
            assert False, "Cart rendering failed after adding item"

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
