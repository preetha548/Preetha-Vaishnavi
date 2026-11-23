# Project navigation

Start with the [full project index](../PROJECTS.md) and [featured projects](../README.md#featured-projects). This directory is a guide, not a monorepo build root.

## Root artifacts retained for compatibility

- `index.html`, `style.css`, `script.js`, `server.js`: duplicate timetable material; the Node server expects a missing `public` directory.
- `login.html`, `dashboard.html`, `current.html`, `option.html`, `payment.html`, `validation.html`, `withdraw.html`, `withdraw-receipt.html`, `func.js`, `money.js`, `val.js`: mixed form/banking demos. Client-side storage/checks are not authentication or a banking system.
- `app.js`: todo code with a missing `library/index.js` import.
- `keyboard.js`, `keyboard.css`, `sketch.js`, `index.js`, CSS/SCSS files: standalone experiments with uncertain entry-point ownership.
- Root Parcel manifest, Vite/PostCSS configs and sandbox/Cypress configs: inconsistent historical setups, not a supported combined application.
- `read.txt`: old machine-specific launch notes, superseded by the brain-tumor guide.

These are intentionally not moved or combined: shared paths are unclear. No important source is removed.
