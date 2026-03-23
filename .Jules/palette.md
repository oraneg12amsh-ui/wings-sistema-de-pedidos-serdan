## 2024-03-23 - Dynamic Accessibility Elements
**Learning:** When checking or adding ARIA labels for accessibility, explicitly inspect JavaScript string templates in addition to static HTML, as many interactive UI components are rendered dynamically.
**Action:** Always `grep` for string literals and DOM construction patterns alongside static elements when doing an accessibility audit.