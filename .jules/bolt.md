## 2024-04-20 - Layout Thrashing in Vanilla JS Loops
**Learning:** In this Vanilla JS codebase, using `.appendChild` directly on the live DOM inside loops causes significant layout thrashing.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them.
