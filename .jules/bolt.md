## 2024-05-18 - DocumentFragment for batching DOM insertions
**Learning:** Using `.appendChild` directly on the live DOM inside loops (e.g., in `filterAndRenderProducts`, `renderList`, `createHearts`) causes significant layout thrashing in this Vanilla JS codebase.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them to the live DOM.
