## 2026-05-12 - Consolidating multiple array reductions into a single iteration

**Learning:** When calculating multiple derived values (like subtotal, items count) from an array in JavaScript, running multiple `Array.prototype.reduce()` calls repeatedly iterates over the same array. For UI rendering cycles that occur frequently (e.g., cart updates), this leads to O(n * m) complexity where m is the number of reductions.
**Action:** Replace multiple `.reduce()` calls with a single `for` loop that computes all necessary aggregations simultaneously, returning a single object with the calculated totals.
