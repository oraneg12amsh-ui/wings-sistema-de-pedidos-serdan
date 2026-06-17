## 2024-06-17 - Batch DOM Insertions
**Learning:** Calling `appendChild` in a loop (e.g., in `filterAndRenderProducts` and `renderList`) causes multiple DOM reflows and layout thrashing, which slows down rendering for longer lists.
**Action:** Use a `DocumentFragment` to batch DOM insertions outside the loop before appending the fragment to the container element.
