## 2024-05-24 - DOM Manipulation Bottlenecks in Vanilla JS Apps
**Learning:** In a single-file Vanilla JS application without a virtual DOM, appending items individually inside loops (e.g., `listEl.appendChild(item)` inside a `forEach`) can cause severe layout thrashing, especially when dealing with product lists or dynamically updating shopping carts.
**Action:** Always batch DOM insertions using `document.createDocumentFragment()` to minimize reflows and repaints when rendering multiple elements at once.
