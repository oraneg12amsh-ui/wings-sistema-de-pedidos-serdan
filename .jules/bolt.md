## 2024-11-20 - Combine Array Iterations
**Learning:** Performing multiple independent `.reduce()` iterations on a large dataset for dependent calculated values (like subtotal, count, taxes) creates an unnecessary O(N) multiplier. A single pass using a `for` loop avoids redundant iterations and allows consolidating calculations into one block.
**Action:** Always compute related total metrics together in a single `for` loop pass (like `getCartTotals()`) instead of running multiple map/filter/reduce operations over the same array.
