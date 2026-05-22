## 2026-05-22 - Debouncing High-Frequency DOM Manipulations
**Learning:** Attaching heavy DOM manipulation operations like rendering product lists directly to raw `input` events causes significant layout thrashing and CPU load, as the list is destroyed and recreated on every keystroke.
**Action:** Always wrap search filtering/rendering logic in a debounce function (e.g., using `setTimeout`) to batch these operations and execute them only after the user pauses typing.
