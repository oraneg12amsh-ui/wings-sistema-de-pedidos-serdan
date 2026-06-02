## 2024-06-02 - Icon-Only Buttons Missing Aria Labels
**Learning:** Icon-only controls in `index.html` (e.g., cart quantity adjustments, modal close buttons using `&times;`, and mobile cart toggles) do not use visible text and must include explicit `aria-label` attributes localized to Spanish (e.g., 'Cerrar carrito', 'Aumentar cantidad') to match the application's primary language.
**Action:** When working on this application, always add explicit, localized `aria-label` attributes to any icon-only interactive elements.
