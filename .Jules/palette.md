## 2024-05-03 - Dynamic ARIA Labels
**Learning:** Icon-only buttons rendered dynamically via Vanilla JS template literals are often overlooked for accessibility. Without `aria-label`, screen readers only announce them as "button," confusing users, especially in interactive lists like shopping carts.
**Action:** Always inject contextual `aria-label` attributes using template variables (e.g., `aria-label="Añadir ${product.name}"`) when building DOM strings to maintain accessibility in dynamic UI components.
