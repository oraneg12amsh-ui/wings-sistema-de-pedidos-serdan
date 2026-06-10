## 2025-02-12 - Debounce Search Input
**Learning:** Frequent, fast typers typing in a search bar trigger an expensive DOM re-render ('filterAndRenderProducts') on every single keystroke. This blocks the main thread on low-end mobile devices common in this user base.
**Action:** When a DOM operation is expensive and tied to keystrokes, introduce a debounce utility function and wrap the event listener callback.
