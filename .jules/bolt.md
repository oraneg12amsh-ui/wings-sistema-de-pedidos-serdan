## 2024-05-24 - Batching DOM updates in Vanilla JS
**Learning:** Appending elements sequentially to the DOM directly inside a loop or iteration (e.g. adding products, rendering cart items, adding animated particles) causes excessive reflows and repaints in Vanilla JavaScript which slows down the UI, especially on low-end devices.
**Action:** Always prefer using a `DocumentFragment` to batch DOM insertions when rendering multiple elements dynamically in Vanilla JS applications, appending elements to the fragment first, and then appending the fragment to the live DOM once.
