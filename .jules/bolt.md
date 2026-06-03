## 2026-06-03 - Batch DOM Insertions with DocumentFragment
**Learning:** In vanilla JavaScript applications with long dynamic lists (like `ALL_PRODUCTS`), calling `appendChild` on an active DOM node inside a loop triggers layout thrashing and continuous repaints.
**Action:** Use `DocumentFragment` to batch DOM node creations inside loops and append the fragment once to the DOM outside the loop to drastically minimize reflows.
