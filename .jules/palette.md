## 2024-05-24 - Missing ARIA labels on Icon-only Controls
**Learning:** Icon-only controls in `index.html` (e.g., cart quantity adjustments, modal close buttons using `&times;`, and mobile cart toggles) lack explicit `aria-label` attributes localized to Spanish. This causes screen reader users to hear ambiguous announcements.
**Action:** Add localized `aria-label` attributes to these controls (e.g., 'Cerrar carrito', 'Aumentar cantidad') to ensure accessibility.
