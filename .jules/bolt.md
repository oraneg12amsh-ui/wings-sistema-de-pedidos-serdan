## 2024-05-17 - DocumentFragment for DOM insertions
**Learning:** Appending DOM nodes individually within a loop causes unnecessary layout thrashing and repaints.
**Action:** Use `DocumentFragment` to batch DOM node insertions. Append nodes to the fragment in the loop, then append the fragment to the container once.
