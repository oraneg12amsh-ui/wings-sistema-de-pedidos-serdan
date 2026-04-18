## 2024-05-18 - Announcing dynamic values seamlessly
**Learning:** When building custom cart UIs with dynamic quantity adjustments in Vanilla JS, updating text content does not naturally trigger screen reader announcements. Using `aria-live="polite"` directly on the wrapper span wrapping dynamic numbers ensures users relying on assistive tech are informed of their quantity and count changes without jarring focus resets.
**Action:** Apply `aria-live="polite"` to dynamically changing spans (like shopping cart counts or line-item quantities) whenever they update via client-side JavaScript.
