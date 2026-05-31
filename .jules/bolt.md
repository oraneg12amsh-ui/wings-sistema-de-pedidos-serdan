## 2026-05-31 - Batching DOM Insertions in renderList
**Learning:** In vanilla JavaScript applications where lists (like a shopping cart or product grid) are repeatedly re-rendered entirely (`listEl.innerHTML = '';` followed by a loop of `appendChild` calls), it causes layout thrashing and multiple reflows, which degrades performance on larger lists.
**Action:** Always use a `DocumentFragment` (`const fragment = document.createDocumentFragment();`) to batch the insertions inside the loop, and append the fragment to the DOM once after the loop completes.
