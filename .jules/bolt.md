## 2024-06-20 - [Performance Optimizations]
**Learning:** Found unnecessary DOM reflows and layout thrashing in list rendering functions (`filterAndRenderProducts` and `renderList`).
**Action:** Always batch DOM insertions using `DocumentFragment` instead of calling `appendChild` within loops.
