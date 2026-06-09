## 2026-06-09 - Added missing aria-labels to icon-only buttons
**Learning:** Icon-only buttons with `&times;` or inline SVGs were frequently missing `aria-label` attributes. Since the site is primarily in Spanish, these must be localized properly (e.g. `aria-label="Cerrar carrito"`).
**Action:** When working on generic UX/a11y improvements, systematically search for buttons with `&times;` or inline SVGs and check for missing `aria-labels`.
