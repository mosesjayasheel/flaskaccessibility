# Accessibility audit: sign-up page (before vs after)

Scope: `/before` and `/after` pages of this Flask app. Standard: WCAG 2.2 AA.

| # | Issue in `before.html` | WCAG SC (level) | Fix in `after.html` |
|---|---|---|---|
| 1 | `<html>` has no `lang` | 3.1.1 (A) | `<html lang="en">` |
| 2 | Logo `<img>` has no `alt` | 1.1.1 (A) | Added `alt="Club logo"` |
| 3 | Inputs use placeholder only, no `<label>` | 1.3.1, 3.3.2 (A) | `<label for>` on each input, plus `autocomplete` |
| 4 | Grey text (#aaa) and white-on-light-blue button fail contrast | 1.4.3 (AA) | Text #1b1f24, link/button #0b57d0 |
| 5 | "Sign up" is a `<div onclick>`: not focusable, no role, no Enter/Space | 2.1.1, 4.1.2 (A) | Real `<button type="submit">` in a `<form>` |
| 6 | `outline:none` removes the focus indicator | 2.4.7 (AA) | `:focus-visible` outline, 3px |
| 7 | Heading jumps from `h1` to `h4` | 1.3.1 (A) | `h1` then `h2` |
| 8 | No `<main>`/`<nav>`/`<header>` landmarks and no skip link | 2.4.1 (A) | Landmarks plus skip link |
| 9 | Invalid email shown only by a red border: no text, not announced | 1.4.1, 3.3.1 (A), 4.1.3 (AA) | Text error via `aria-describedby`, `aria-invalid`, focus moved to first error, `role="status"` on success |

Total: 9 issues found, 9 fixed.
