# Node.js experiments

[Node project inventory](../PROJECTS.md#nodejs--backend-experiments) lists the actual Node source folders. Most serve static HTML; Cycle Marathon, Friend, Sports Sponsorship and Tango also have form/data routes.

Several folders lack dependency manifests or `public` directories. Cycle Marathon declares Express and has a public UI but lacks `data/` and input/access controls. Flight Booking declares Express but lacks `public/`. Diary and Letter box use Node’s built-in `http` module.

There is no supported repository-wide install/start command. Do not install dependencies at root to mask project-specific gaps. Review [SECURITY_NOTES.md](../SECURITY_NOTES.md) before exposing any server.
