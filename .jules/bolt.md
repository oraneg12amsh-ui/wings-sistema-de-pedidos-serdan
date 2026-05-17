
## 2024-05-18 - Debounce search input
**Learning:** Attaching heavy DOM manipulation functions directly to 'input' events causes layout thrashing and high CPU usage during rapid typing.
**Action:** Always wrap search/filter input handlers in a `setTimeout` debounce to group fast keystrokes into a single render update.
