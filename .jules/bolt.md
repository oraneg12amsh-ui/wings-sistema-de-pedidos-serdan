## 2024-05-18 - Debouncing Search Inputs
**Learning:** Frequent, heavy DOM manipulations triggered by synchronous event listeners (like 'input' on a search bar) can cause severe layout thrashing and CPU load, especially if the filtering logic rebuilds a large portion of the DOM on every keystroke.
**Action:** Always implement a debounce strategy (e.g., using `setTimeout` and `clearTimeout`) on high-frequency input events that trigger expensive filtering or rendering operations to batch the updates and significantly improve client-side rendering performance.
