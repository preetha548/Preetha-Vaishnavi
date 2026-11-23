# Rock Paper Scissors

**Status: learning project.** A small browser game chosen for its clear, implemented core interaction rather than visual complexity.

## Features

- Rock, paper and scissors choices against a random computer move.
- Win, loss and tie comparison for all nine move combinations.
- Cumulative score stored under `score` in localStorage.
- Reset control that clears the counters and stored score.

## Technologies and run instructions

HTML and vanilla JavaScript; no backend or external script is required.

From this directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. The legacy package manifest also provides a static `serve` command, but it is optional for this page; it does not provide an application backend.

## Verify the game rules

From this directory, with Node.js 20 or newer:

```sh
node --test tests/game.test.cjs
```

The checks execute the original inline script in isolated contexts, cover all nine move combinations, verify reload persistence and reset, and use mocked storage/alerts.

## Screenshots

No project-local screenshot is committed. The current UI is a deliberately small set of buttons with result alerts.

## Limitations

Scores are local to a browser/origin, not an online account or leaderboard. The generic storage key may collide when other demos share an origin. Malformed storage or disabled storage is not handled in the original code. Results use browser alerts rather than an accessible inline scoreboard.

## Next improvements

Add validated, namespaced storage with graceful failure handling, an inline result region, and keyboard/mobile polish. Keep the simple game rules understandable and test all move combinations if they are changed.
