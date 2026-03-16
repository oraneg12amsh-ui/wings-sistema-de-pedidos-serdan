## 2023-11-20 - [DOM Reflow Bottleneck]
**Learning:** Found that rendering multiple elements inside a loop (like products or hearts) and appending them individually to the container triggers multiple synchronous layout recalcs and repaints, which is a common frontend performance bottleneck.
**Action:** Always batch DOM insertions using `DocumentFragment`. Append new elements to the fragment within the loop, and append the complete fragment to the container once outside the loop to minimize layout thrashing.
