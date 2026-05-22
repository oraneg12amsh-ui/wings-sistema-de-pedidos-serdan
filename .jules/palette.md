## 2023-10-27 - Icon-Only Button ARIA Labels
**Learning:** Screen readers and accessibility tools cannot interpret the purpose of icon-only buttons (like `&times;` or SVG icons) without visible text. This is a common pattern in this repository for modals, mobile toggles, and cart controls.
**Action:** When adding or modifying interactive UI components that lack visible descriptive text, ensure `aria-label` attributes are explicitly added (and localized to the application's language, e.g., Spanish) to convey the button's action to assistive technologies.
