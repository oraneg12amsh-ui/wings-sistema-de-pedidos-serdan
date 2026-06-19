## 2024-05-24 - Accessibility improvements
**Learning:** Found an accessibility issue pattern specific to this app's components: icon-only controls in `index.html` (e.g., cart quantity adjustments, modal close buttons using `&times;`, and mobile cart toggles) must include explicit `aria-label` attributes localized to Spanish (e.g., 'Cerrar carrito', 'Aumentar cantidad') to match the application's primary language.
**Action:** When working on UI changes, always remember to verify and add Spanish-localized `aria-label`s for any interactive icon elements.
