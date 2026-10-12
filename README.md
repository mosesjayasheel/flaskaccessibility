# Flask Accessibility Remediation Demo

A small Flask app that serves a sign-up page twice: `/before` has 9 deliberate WCAG failures and `/after` fixes each one. `AUDIT.md` maps every issue to its WCAG criterion.

## Run
```bash
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000/before and http://127.0.0.1:5000/after.

## Issues covered
Missing `lang`, missing alt text, placeholder-only inputs, low contrast, a `div` used as a button, removed focus outline, skipped heading levels, missing landmarks and skip link, and color-only error feedback. See `AUDIT.md`.


