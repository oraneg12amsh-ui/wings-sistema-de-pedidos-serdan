
## 2024-05-15 - ARIA Labels in Dynamic Template Strings
**Learning:** When improving accessibility in Vanilla JS applications, static HTML is only half the picture. Many interactive components (like cart item controls: increase, decrease, remove) are rendered dynamically via JavaScript string templates. It's critical to inspect these templates, not just the static `index.html` skeleton, to ensure all icon-only buttons receive proper `aria-label`s.
**Action:** Always `grep` for `<button` inside JavaScript template literals in addition to static HTML when checking for accessibility gaps.
