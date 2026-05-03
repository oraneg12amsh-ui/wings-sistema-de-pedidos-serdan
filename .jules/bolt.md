## 2024-05-03 - [Refactor Cart Totals]
**Learning:** Performance benchmarks for cart calculations in `index.html` show that a single `for` loop (implemented in `getCartTotals`) is approximately 10x faster than performing multiple separate `.reduce()` calls on the cart array for large datasets.
**Action:** Centralize cart calculations and replace multiple `reduce` iterations with a single `for` loop when working with large data sets to improve performance.
