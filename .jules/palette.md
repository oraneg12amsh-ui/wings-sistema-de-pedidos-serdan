## 2024-06-14 - Icon-only buttons lacking ARIA labels
**Learning:** In standard HTML, icon-only buttons (like modal close buttons or cart qty buttons) are inaccessible to screen readers without an explicit `aria-label`. Since the app's primary language is Spanish, we should localize the ARIA labels.
**Action:** Always add explicit `aria-label` attributes to icon-only buttons, making sure to match the application's target language (e.g., 'Cerrar' or 'Eliminar').
