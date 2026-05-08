## 2024-05-08 - Icon-Only Button ARIA Labels
**Learning:** Found multiple instances where critical interaction buttons (like close modals and cart controls) were rendered as icon-only without `aria-label`s, making them invisible to screen readers.
**Action:** Always verify icon-only UI elements have descriptive `aria-label` attributes to ensure keyboard and screen reader accessibility, particularly within dynamic JS template literals.
