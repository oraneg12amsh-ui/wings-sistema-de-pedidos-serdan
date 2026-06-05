## 2024-05-24 - DOM Layout Thrashing Optimization
**Learning:** Using `appendChild` directly on the DOM inside loops (like in `filterAndRenderProducts` and `renderList`) causes severe layout thrashing and repetitive reflows. This degrades performance significantly as the list sizes grow.
**Action:** Use `DocumentFragment` to batch DOM insertions outside the loop. This minimizes reflows to just one single operation when appending the fragment to the DOM, improving rendering speed.
