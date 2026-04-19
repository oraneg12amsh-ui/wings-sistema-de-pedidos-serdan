## 2024-04-19 - DocumentFragment prevents layout thrashing
**Learning:** In this Vanilla JS codebase, using `.appendChild` directly on the live DOM inside loops causes significant layout thrashing.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them.
