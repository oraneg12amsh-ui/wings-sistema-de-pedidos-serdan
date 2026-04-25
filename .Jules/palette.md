## 2024-05-24 - Screen Reader Compatibility with Vanilla JS String Interpolation
**Learning:** When injecting ARIA attributes (like `aria-label` or `aria-live`) into dynamically generated Vanilla JS content, patch the string interpolation logic directly within the DOM-generating functions instead of attempting post-render `querySelector` updates to ensure reliability.
**Action:** Always search for and modify the HTML template literals directly within the JavaScript functions responsible for rendering dynamic content (e.g., `renderList`) to apply accessibility attributes.
