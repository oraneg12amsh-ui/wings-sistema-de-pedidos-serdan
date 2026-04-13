## 2025-04-13 - Dynamic ARIA Attributes

**Learning:** When modifying Vanilla JS applications with complex string literals containing dynamic data (e.g., shopping cart quantities), we can effectively inject contextual ARIA attributes like `aria-label="Agregar ${product.name}"` or `aria-live="polite"` directly into the string interpolation logic before it's attached to the DOM.

**Action:** When implementing micro-UX features in single-file or highly dynamic setups, rely on `replace_with_git_merge_diff` to accurately locate and patch string literals in DOM-generating functions to inject a11y data dynamically instead of relying on post-render querySelector updates.
