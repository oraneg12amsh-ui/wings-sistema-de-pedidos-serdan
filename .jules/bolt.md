## 2024-06-07 - Inefficient DOM manipulations
**Learning:** `appendChild` is called inside a loop for both `filterAndRenderProducts` and `renderList`, causing layout thrashing and unnecessary DOM reflows.
**Action:** Use a `DocumentFragment` to batch DOM insertions outside the loop.
