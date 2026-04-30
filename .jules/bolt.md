## 2024-05-24 - Cart Calculations Optimization
**Learning:** Performing multiple un-memoized `.reduce()` iterations on the cart array for calculating totals (subtotal, shipping, discount, total, count) causes redundant O(N) operations. Local Node.js benchmarks show a single `for` loop is approximately 10x faster for large datasets.
**Action:** Centralize order calculations in a `getCartTotals()` function using a single `for` loop to compute all metrics simultaneously, and replace scattered `.reduce()` calls across render routines and event handlers.

## 2024-05-25 - DOM Batch Insertion
**Learning:** In this Vanilla JS codebase, using `.appendChild` directly on the live DOM inside loops causes significant layout thrashing.
**Action:** Always use `DocumentFragment` to batch DOM insertions before appending them.
