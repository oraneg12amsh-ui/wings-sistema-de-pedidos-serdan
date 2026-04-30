## 2025-02-12 - ARIA labels in Vanilla JS Template Literals
**Learning:** Vanilla JS template literals generating icon-only buttons (`+`, `-`, `&times;`) create an accessibility anti-pattern if they don't interpolate descriptive `aria-label`s directly during DOM generation.
**Action:** When dynamically generating UI elements with icon-only buttons using Vanilla JS template literals, ensure that `aria-label` attributes are added directly into the HTML string before the DOM is updated, possibly dynamically inserting variable values (e.g. `aria-label="Agregar ${product.name} extra"`).
