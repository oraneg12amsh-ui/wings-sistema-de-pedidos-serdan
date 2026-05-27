## 2024-05-27 - Batch DOM insertions with DocumentFragment
**Learning:** In vanilla JS loops appending large amounts of elements (like products or cart items), calling `appendChild` directly on an existing DOM node causes layout thrashing and performance degradation.
**Action:** Always create a `DocumentFragment` (`document.createDocumentFragment()`), append all elements to it during the loop, and then call `appendChild` on the actual DOM node once after the loop.
