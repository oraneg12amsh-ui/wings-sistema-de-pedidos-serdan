## 2023-10-27 - Layout Thrashing in Vanilla JS Loops
**Learning:** In this Vanilla JS codebase, using `.appendChild` directly on the live DOM inside loops (e.g., in `createHearts`, `filterAndRenderProducts`, and `renderList`) causes significant layout thrashing.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them to the live DOM, and ensure inline comments explain the rationale (e.g., `// Optimization: Use DocumentFragment to batch DOM insertions to prevent layout thrashing`).
