## 2024-06-14 - Batch DOM insertions with DocumentFragment
**Learning:** Appending items individually to the DOM inside loops (e.g., `appendChild` in `filterAndRenderProducts` and `renderList`) causes layout thrashing and reflows.
**Action:** Use a `DocumentFragment` to batch insertions and only append to the main DOM once after the loop.
