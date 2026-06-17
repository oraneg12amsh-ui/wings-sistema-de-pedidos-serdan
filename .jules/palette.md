## 2024-06-17 - Add ARIA Labels to Icon-Only Buttons
**Learning:** Found several icon-only buttons (close modals, mobile cart toggle, increase/decrease quantity, remove from cart, add extra) missing accessible names. These buttons are rendered both statically in HTML and dynamically via JavaScript.
**Action:** Adding `aria-label` attributes to these icon-only buttons using localized Spanish text, as standard for UX best practices, to improve accessibility for screen readers.
