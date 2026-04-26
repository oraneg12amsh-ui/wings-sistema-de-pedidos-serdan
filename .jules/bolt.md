## 2024-04-26 - Prevent Layout Thrashing with DocumentFragment
**Learning:** In Vanilla JS, appending elements directly to the live DOM inside loops (using `.appendChild`) triggers multiple reflows and repaints, leading to significant layout thrashing and poor rendering performance.
**Action:** Always use `DocumentFragment` to batch DOM node creations and insertions within loops, appending the entire fragment to the live DOM exactly once to eliminate redundant layouts.
