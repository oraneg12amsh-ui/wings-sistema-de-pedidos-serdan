## 2024-05-14 - Initial Palette Journal Created
**Learning:** Document critical UX/accessibility learnings here.
**Action:** Always check here before starting a UX task.

## 2024-05-14 - Dynamic Contextual ARIA Labels & Live Regions
**Learning:** Icon-only buttons within dynamically generated JavaScript string templates must have explicitly injected contextual ARIA labels (e.g., `aria-label="Agregar ${product.name} como extra"`). Additionally, dynamic text updates (like shopping cart item quantities) must be wrapped in elements with `aria-live="polite"` so screen readers correctly announce the changes without requiring a focus shift.
**Action:** When adding or verifying interactive UI components rendered via Vanilla JS template literals, verify that all button controls without visual text labels contain descriptive `aria-label`s using string interpolation. Similarly, ensure any dynamically updating numbers or status messages use `aria-live`.
