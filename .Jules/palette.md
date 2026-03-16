## 2024-03-16 - Add aria-label to icon-only buttons
**Learning:** Icon-only buttons (like those using SVGs or HTML entities like `&times;`) are often read by screen readers in unhelpful ways (like "times" or "unlabeled graphic") or completely skipped. Adding a descriptive `aria-label` ensures screen reader users understand the button's purpose without changing the visual layout.
**Action:** Always verify icon-only buttons have an `aria-label` or `title` (or hidden descriptive text) to maintain accessibility.
