## 2024-05-19 - Batching DOM Insertions with DocumentFragment

**Learning:** When rendering lists of items in vanilla JavaScript using `createElement` and `appendChild` within a loop, directly appending each element to the DOM container causes significant layout thrashing and unnecessary DOM reflows. This performance bottleneck is a common pattern when dynamically rendering large lists or complex elements like the starry background and product cards.

**Action:** When inserting multiple DOM elements, create a `DocumentFragment` (`document.createDocumentFragment()`), append the elements to the fragment inside the loop, and then append the entire fragment to the actual DOM container in a single operation after the loop.
