## 2024-06-13 - Icon-only buttons lack ARIA labels
**Learning:** Found multiple icon-only buttons (like mobile cart toggle, modal close buttons) missing `aria-label` attributes. This breaks accessibility for screen reader users as they have no context for these actions.
**Action:** Always add descriptive `aria-label`s to icon-only controls, keeping localization in mind (e.g. Spanish for this app).
