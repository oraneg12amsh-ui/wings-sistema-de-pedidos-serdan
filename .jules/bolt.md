
## 2024-05-18 - Native Event Debouncing for Search Optimization
**Learning:** In Vanilla JS applications, triggering expensive operations like `filterAndRenderProducts` (which manipulates the DOM heavily) on every single keystroke during a search input event causes significant layout thrashing and CPU load. Centralized debouncing using a simple `setTimeout` is a lightweight, dependency-free solution.
**Action:** When implementing or reviewing search inputs in vanilla JS, always ensure the event listener is debounced (typically ~300ms) to batch DOM updates and prevent performance degradation.
