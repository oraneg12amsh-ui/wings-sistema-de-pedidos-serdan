## 2024-05-24 - Debouncing Global Event Listeners
**Learning:** Attaching a synchronous, expensive DOM manipulation function directly to an `input` event on a search bar causes severe layout thrashing and CPU spikes because the function executes on every single keystroke.
**Action:** Always wrap frequent UI event listeners (like typing in a search bar or scrolling) in a `setTimeout`/`clearTimeout` debounce wrapper to batch executions.
