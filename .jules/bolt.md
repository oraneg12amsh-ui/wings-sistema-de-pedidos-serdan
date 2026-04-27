
## 2024-04-27 - Centralize Cart Totals Calculation
**Learning:** In Vanilla JS applications, redundant un-memoized `.reduce()` loops over the same state array (like `state.cart`) scattered across multiple UI update functions (`updateTotals`, `updateCambio`, `renderCart`, form handlers) cause unnecessary performance overhead as the array grows.
**Action:** Centralize the logic into a single function (`getCartTotals`) that uses one efficient `for` loop to compute all related metrics (subtotal, shipping, discount, total, count) and return them as an object. Refactor all scattered `.reduce()` calls to destructure the needed values from this centralized function.
