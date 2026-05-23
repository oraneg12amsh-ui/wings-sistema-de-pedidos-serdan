## 2024-05-23 - Search Bar Debounce
**Learning:** The `dom.searchBar` event listener in `index.html` was triggering `filterAndRenderProducts()` on every single keystroke, causing unnecessary re-renders, layout thrashing, and high CPU load for users.
**Action:** Always add a native debounce (e.g., using a 300ms `setTimeout`) to frequent events like search input to prevent performance bottlenecks without significantly affecting UX.
