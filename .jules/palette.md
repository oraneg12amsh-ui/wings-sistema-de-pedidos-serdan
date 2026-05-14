## 2024-05-24 - ARIA labels in dynamic template strings
**Learning:** When adding ARIA labels to dynamically generated HTML (like template literals inside JavaScript mapping functions), testing with standard UI tools can be complex if the elements are deeply nested or rely on complex application state.
**Action:** Use regex matching directly on the source file or extracted script blocks (e.g., using a standalone Node.js script `test.mjs`) to verify the exact string structures of the dynamically injected HTML as a reliable fallback for verification.
