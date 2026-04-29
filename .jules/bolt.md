## 2025-02-18 - [Optimization of Array Comparison in addToCart]
**Learning:** Using `JSON.stringify()` for array comparison inside loops or frequent operations like `.find()` introduces unnecessary overhead. For simple array comparisons where elements are primitives, a shallow comparison loop is significantly faster.
**Action:** Replace `JSON.stringify` with a custom `areArraysEqual` helper function for shallow comparisons in similar iterative scenarios to boost performance.
