## 2024-05-24 - DOM Insertion Optimization
**Learning:** Appending elements dynamically one-by-one inside a loop causes excessive layout reflows and repaints in Vanilla JS.
**Action:** Always batch DOM insertions using a `DocumentFragment` when rendering lists like product catalogs or cart items.
