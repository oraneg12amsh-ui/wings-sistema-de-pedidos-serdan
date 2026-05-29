## 2025-02-18 - Batch DOM manipulations to prevent layout thrashing
**Learning:** Frequent DOM insertions (like using `.appendChild` in loops) cause unnecessary reflows and repaints in vanilla JS, degrading performance, especially on low-end devices or with large product lists.
**Action:** Use `DocumentFragment` to batch DOM operations before appending to the real DOM, ensuring a single reflow/repaint for the entire list update.
