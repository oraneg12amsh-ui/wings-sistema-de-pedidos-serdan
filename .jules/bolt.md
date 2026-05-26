
## 2024-05-26 - Prevent Layout Thrashing with DocumentFragment
**Learning:** Calling `appendChild` on a live DOM node inside a loop causes the browser to recalculate layout and reflow the page on every single iteration, leading to massive performance bottlenecks and layout thrashing, especially in generic rendering functions like `filterAndRenderProducts` and `renderList` in Vanilla JS apps.
**Action:** Always batch DOM insertions using `document.createDocumentFragment()`. Append all elements to the fragment inside the loop, and then append the fragment to the target container once after the loop completes to trigger only a single reflow.
