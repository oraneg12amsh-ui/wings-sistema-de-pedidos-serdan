## 2024-06-25 - Rely on Built-in Parsers

**Learning:** The Python `bs4` (BeautifulSoup) library is not pre-installed in the environment. When writing custom validation scripts to parse HTML, attempting to use third-party libraries will cause failures and require workarounds.
**Action:** Default to using standard Node.js string/regex manipulation or built-in Python modules (like `re` or `html.parser`) for lightweight HTML parsing and validation tasks, rather than assuming external dependencies are available.
