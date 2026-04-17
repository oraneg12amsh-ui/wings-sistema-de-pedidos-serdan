## 2024-04-17 - DocumentFragment DOM Batching
**Learning:** Using `.appendChild` directly on the DOM inside loops (like rendering product lists or UI elements) causes significant layout thrashing in this Vanilla JS codebase.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them to the live DOM.
