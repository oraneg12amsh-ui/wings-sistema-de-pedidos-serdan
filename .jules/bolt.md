## 2025-04-18 - DocumentFragment DOM Batching
**Learning:** In this Vanilla JS codebase, using `.appendChild` directly on the live DOM inside loops (like in `renderList`, `filterAndRenderProducts`, and `createHearts`) causes significant layout thrashing.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them to the live DOM when iterating over arrays to generate UI elements.
