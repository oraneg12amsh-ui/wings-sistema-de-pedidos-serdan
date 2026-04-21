## 2024-05-24 - Centralize Cart Calculation with Memoization
**Learning:** Performing multiple `.reduce()` calls on `state.cart` across different functions (`renderCart`, `updateTotals`, `updateCambio`) is redundant and negatively impacts performance, especially as cart size grows. A single `for` loop computing `sub`, `ship`, `disc`, `total`, and `count` simultaneously is ~10x faster.
**Action:** Always centralize array-based aggregate calculations into a single, optimized function (`getCartTotals`) and pass the precalculated results where necessary.
