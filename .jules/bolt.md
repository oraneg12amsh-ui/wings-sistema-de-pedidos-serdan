## 2024-05-19 - Batching DOM Insertions with DocumentFragment

**Learning:** When repeatedly appending elements to the DOM in a loop (like iterating through a product list or rendering a shopping cart), calling `appendChild` directly on a live DOM node causes frequent layout thrashing and reflows.

**Action:** Always batch DOM insertions using `DocumentFragment`. Create a `const fragment = document.createDocumentFragment();`, append elements to the fragment during the loop, and then call `appendChild` on the target DOM node only once with the populated fragment.
