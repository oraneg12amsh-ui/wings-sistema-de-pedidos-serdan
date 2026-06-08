## 2024-05-24 - DOM Manipulation Optimizations in Loops
**Learning:** Appending directly to the DOM within loops (like rendering list items or product cards) causes multiple reflows and repaints, drastically reducing performance on list renders. In vanilla JS without virtual DOMs, this is a significant bottleneck.
**Action:** Always batch DOM insertions using `DocumentFragment` before appending to the live DOM when iterating over arrays to generate HTML elements.
