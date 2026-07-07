## 2024-07-08 - Added missing ARIA labels
**Learning:** Found several icon-only buttons lacking `aria-label`s, such as close modal buttons (`&times;`, SVG icons) and cart interaction buttons (+, -, remove).
**Action:** Always verify icon-only buttons have descriptive `aria-label` attributes to ensure screen reader accessibility. Ensure Spanish localization for the aria-labels to match the rest of the application context.
