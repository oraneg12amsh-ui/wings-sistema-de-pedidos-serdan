## 2024-05-24 - DocumentFragment over appendChild
**Learning:** Adding elements to the DOM in a loop using `appendChild` triggers a reflow for every element. Using `DocumentFragment` and appending them all at once avoids this.
**Action:** Use `DocumentFragment` when rendering lists.
