## 2024-05-29 - Missing aria-label for icon-only buttons
**Learning:** Icon-only controls in `index.html` (e.g., cart quantity adjustments, modal close buttons using `&times;`, and mobile cart toggles) do not use visible text and must include explicit `aria-label` attributes localized to Spanish (e.g., "Cerrar carrito", "Aumentar cantidad") to match the applications primary language.
**Action:** Always add localized `aria-label` attributes to icon-only buttons or those with non-semantic text (like `&times;`) to ensure accessibility for screen readers.
