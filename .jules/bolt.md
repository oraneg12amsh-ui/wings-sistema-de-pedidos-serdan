## 2024-05-18 - DocumentFragment for DOM Insertions
**Learning:** In vanilla JS, iterating over an array to generate elements and appending them directly to the DOM causes layout thrashing and reflows.
**Action:** When rendering lists like products or cart items, use `document.createDocumentFragment()` to batch append operations into a single DOM update.
