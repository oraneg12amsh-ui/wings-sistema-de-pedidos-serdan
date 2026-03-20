import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Using a mobile viewport to see mobile cart button
        page = await browser.new_page(viewport={"width": 375, "height": 812})
        await page.goto("http://localhost:8000")

        # Wait for page load and dismiss the intro overlay as instructed in memory
        await page.wait_for_selector("#intro-overlay")
        await page.click("#intro-overlay")
        await page.wait_for_timeout(1000) # Give overlay time to fade out

        # Check mobile cart button
        mobile_cart_btn = page.locator("#mobile-cart-button")
        print("Mobile Cart aria-label:", await mobile_cart_btn.get_attribute("aria-label"))

        # Click it
        await mobile_cart_btn.click(force=True)
        await page.wait_for_timeout(500)

        # Check close button
        close_btn = page.locator("#close-mobile-cart-button")
        print("Close Mobile Cart aria-label:", await close_btn.get_attribute("aria-label"))

        await close_btn.click(force=True)

        await browser.close()

asyncio.run(run())
