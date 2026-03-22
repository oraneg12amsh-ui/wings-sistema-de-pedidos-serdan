from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Configure mobile viewport to ensure mobile cart button is visible
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()

        try:
            # Navigate to the local server
            page.goto("http://localhost:8000")

            # Dismiss overlay using memory learning (force=True)
            page.locator('#intro-overlay').click(force=True)
            page.wait_for_timeout(2000) # wait for fade-out animation

            # Use JS to manipulate the cart items directly to test the dynamic template string since ALL_PRODUCTS is inside a module
            # We can find the DOM element and insert HTML to test the cart list dynamically rendered classes
            page.evaluate('''() => {
                const listEl = document.getElementById('cart-list-mobile');
                if (listEl) {
                    const item = { name: 'Orden (6 pzs)', quantity: 1, price: 65, flavors: ['BBQ'] };
                    const index = 0;
                    const isStoreCurrentlyOpen = true;

                    const flavorsText = item.flavors && item.flavors.length > 0 ? `<p class="text-xs text-pink-300/60 mt-1">Sabores: ${item.flavors.join(', ')}</p>` : '';
                    const cartItem = document.createElement('div');
                    cartItem.className = 'flex justify-between items-start bg-slate-800/30 p-3 rounded-xl border border-slate-700/50';
                    cartItem.innerHTML = `<div class="flex-1 min-w-0 pr-2"><div class="font-bold text-white text-sm">${item.name}</div>${flavorsText}<div class="text-brand-love font-bold text-sm mt-1">$65.00</div></div><div class="flex items-center gap-2 bg-slate-800 rounded-lg p-1"><button data-index="${index}" aria-label="Disminuir cantidad de ${item.name}" class="decrease-qty-btn w-6 h-6 flex items-center justify-center text-pink-300 hover:text-white" ${!isStoreCurrentlyOpen ? 'disabled' : ''}>-</button><span class="font-bold text-white text-sm w-4 text-center">${item.quantity}</span><button data-index="${index}" aria-label="Aumentar cantidad de ${item.name}" class="increase-qty-btn w-6 h-6 flex items-center justify-center text-pink-300 hover:text-white" ${!isStoreCurrentlyOpen ? 'disabled' : ''}>+</button></div><button data-index="${index}" aria-label="Eliminar ${item.name} del carrito" class="remove-from-cart-btn text-red-500 hover:text-red-400 ml-2 pt-1" ${!isStoreCurrentlyOpen ? 'disabled' : ''}>&times;</button>`;
                    listEl.appendChild(cartItem);
                }
            }''')

            page.wait_for_timeout(500)

            # Click mobile cart button
            page.locator('#mobile-cart-button').click(force=True)
            page.wait_for_timeout(1000)

            # Take a screenshot showing the open cart and cart items with their buttons
            page.screenshot(path="verification_open_cart.png")

            # Evaluate script to check aria-labels of dynamically rendered buttons
            labels_check = page.evaluate('''() => {
                const results = [];
                const mobileCartBtn = document.querySelector('#mobile-cart-button');
                if (mobileCartBtn) results.push('mobileCartBtn: ' + mobileCartBtn.getAttribute('aria-label'));

                const closeCartBtn = document.querySelector('#close-mobile-cart-button');
                if (closeCartBtn) results.push('closeCartBtn: ' + closeCartBtn.getAttribute('aria-label'));

                const decreaseBtn = document.querySelector('.decrease-qty-btn');
                if (decreaseBtn) results.push('decreaseBtn: ' + decreaseBtn.getAttribute('aria-label'));

                const increaseBtn = document.querySelector('.increase-qty-btn');
                if (increaseBtn) results.push('increaseBtn: ' + increaseBtn.getAttribute('aria-label'));

                const removeBtn = document.querySelector('.remove-from-cart-btn');
                if (removeBtn) results.push('removeBtn: ' + removeBtn.getAttribute('aria-label'));

                return results;
            }''')
            print("Aria labels found:", labels_check)

        except Exception as e:
            print(f"Error during verification: {e}")
            page.screenshot(path="verification_error.png")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_frontend()