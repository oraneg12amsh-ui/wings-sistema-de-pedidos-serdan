## 2024-03-24 - Dynamic ARIA Labeling Check
**Learning:** Many interactive UI components (like cart buttons, quantity adjusters) in this application are rendered via JavaScript string templates rather than existing statically in HTML. When performing accessibility audits for missing `aria-label`s, inspecting only the static DOM is insufficient and will miss critical icon-only buttons.
**Action:** Always explicitly inspect JavaScript string templates (`grep` or read JS functions returning HTML strings) in addition to static HTML when checking or adding ARIA labels for accessibility.
