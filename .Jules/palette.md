## 2024-05-24 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** Interactive icon-only buttons generated via Vanilla JS string templates in this app often omit `aria-label` and keyboard focus states.
**Action:** Add `aria-label` and Tailwind focus ring classes (`focus:outline-none focus:ring-2 focus:ring-brand-love`) to dynamically rendered icon-only buttons.
