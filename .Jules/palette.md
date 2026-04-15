## 2026-04-15 - Dynamic Aria Labels in Templates
**Learning:** When performing accessibility sweeps, icon-only buttons generated dynamically via JavaScript template strings require contextual ARIA labels (e.g., `aria-label="Añadir ${product.name}"`), in addition to static HTML buttons.
**Action:** Always search JavaScript template logic (``) for interactive elements missing ARIA attributes, especially when dealing with Vanilla JS rendering patterns.
