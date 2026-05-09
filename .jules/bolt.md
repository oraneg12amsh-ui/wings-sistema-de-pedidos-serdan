## 2024-05-24 - Batch DOM insertions with DocumentFragment
**Learning:** Using `.appendChild` directly inside loops causes layout thrashing and performance degradation, especially when generating large lists or complex visual elements (like the stars particles and product catalog).
**Action:** Always batch DOM insertions inside loops using `document.createDocumentFragment()` and append the fragment to the container once outside the loop to minimize repaints.
