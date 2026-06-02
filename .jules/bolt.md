## 2024-06-12 - DOM Manipulation Optimization
**Learning:** In vanilla JS applications rendering lists of DOM elements (like product listings, cart items, or animated particles) directly with `appendChild` inside a loop causes layout thrashing and unnecessary reflows.
**Action:** Use `DocumentFragment` to batch DOM insertions outside the loop, reducing performance overhead by making a single insertion instead of multiple.
