## 2024-06-16 - DOM Batching for List Rendering
**Learning:** `filterAndRenderProducts` and `renderList` repeatedly call `appendChild` inside a loop, causing layout thrashing and poor performance on lists. This causes many recalculations of layout since it renders the products list (e.g. `ALL_PRODUCTS.forEach` or `state.cart.forEach`).
**Action:** Use a `DocumentFragment` to batch DOM insertions to minimize reflows and repaints.
