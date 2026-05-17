## 2024-05-24 - Added ARIA labels to icon-only controls
**Learning:** Icon-only controls in `index.html` (e.g., cart quantity adjustments, modal close buttons using `&times;`, and mobile cart toggles) do not use visible text and must include explicit `aria-label` attributes for accessibility. When these are inside dynamically generated Vanilla JS template literals, standard HTML verification tools may struggle.
**Action:** Use Python script with regex to verify string structure of inline template literals. Ensure the language used matches the app's locale (Spanish).
