
## 2024-05-30 - Localized ARIA Labels for Icon-Only Buttons
**Learning:** Icon-only controls (like close buttons, cart quantity adjustments) must have explicit `aria-label` attributes to be accessible to screen readers. Crucially, these labels must be localized to match the application's primary language (e.g., Spanish for this repo) to ensure a coherent experience for users relying on assistive technologies.
**Action:** Always verify that interactive elements without visible text have descriptive, localized `aria-label`s or visually hidden text to provide context for screen reader users.
