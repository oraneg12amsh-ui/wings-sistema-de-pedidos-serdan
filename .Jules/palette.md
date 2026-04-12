## 2024-05-18 - ARIA labels in dynamic templates
**Learning:** Checking ARIA properties locally using `page.evaluate` and `getAttribute` in Playwright is a robust alternative to clicking around, especially when click intercepts like `#intro-overlay` block UI interactions.
**Action:** When testing dynamic accessibility changes under UI overlays, mock state globally and read DOM attributes directly rather than strictly navigating user flows.
