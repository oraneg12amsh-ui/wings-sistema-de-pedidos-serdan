## 2024-03-22 - Adding ARIA labels to dynamically rendered and hard-coded icon-only buttons
**Learning:** Found that icon-only buttons need aria labels. In this specific app, some are dynamically rendered within string templates in javascript while others are hard-coded in HTML.
**Action:** When searching for missing ARIA labels, remember to inspect JS string templates alongside HTML elements to ensure accessibility for dynamically injected components.
