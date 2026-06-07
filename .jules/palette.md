## 2024-05-18 - Missing ARIA labels on Icon-only Controls
**Learning:** Found several icon-only buttons (close buttons, remove item buttons, mobile cart toggle) in index.html that are missing `aria-label` attributes or equivalent accessibility features. The mobile app has many such interactive elements and without an accessible name, they are practically invisible to screen readers.
**Action:** Adding explicit Spanish ARIA labels to these elements.
