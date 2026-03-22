## 2026-03-22 - ARIA labels in dynamic templates
**Learning:** Interactive UI components are often rendered dynamically via JavaScript templates. Accessibility checks and `aria-label` additions must explicitly target these dynamic strings, not just the static HTML.
**Action:** Always inspect JS template strings when checking or adding ARIA labels for accessibility, as many interactive UI components (like cart actions) are rendered dynamically.
