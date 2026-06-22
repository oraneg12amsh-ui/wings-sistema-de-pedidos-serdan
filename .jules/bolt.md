## 2026-06-22 - Batch DOM insertions with DocumentFragment
**Learning:** Found an opportunity to improve frontend rendering performance by batching DOM insertions in the `filterAndRenderProducts` and `renderList` loops. Appending elements directly inside loops triggers layout thrashing and reflows.
**Action:** Used `DocumentFragment` to batch DOM operations and appended the fragment to the DOM once outside the loops. Always look for loops performing single DOM insertions and replace with fragment batching for vanilla JS rendering optimizations.
