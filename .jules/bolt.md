## 2025-05-18 - DOM Batching for List Rendering
**Learning:** Rendering long lists by repeatedly calling `appendChild` on the parent container directly within a loop causes unnecessary layout thrashing and reflows, which can significantly degrade frontend performance.
**Action:** Use a `DocumentFragment` to batch DOM node creations in memory, and then append the entire fragment to the parent container once after the loop finishes.
