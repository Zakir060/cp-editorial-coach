# CP Editorial Coach UI Prototype

This package contains a polished front-end prototype for the **CP Editorial Coach** product.

## Files
- `index.html` — interactive single-page prototype
- `styles.css` — responsive visual system
- `script.js` — interaction logic, local state, language/theme toggles, unlock flow

## Product intent
The UI is designed for a user who pastes a Codeforces link and wants help in layers:
1. Hint 1
2. Hint 2
3. Approach
4. Full explanation
5. Why it works
6. Complexity
7. Edge cases
8. C++ solution

The interface keeps the **coach** feeling stronger than a simple solution generator.

## Main UX decisions
- **Spoiler-safe progression**: in guided mode, only the next logical step is unlocked.
- **Fast-track mode**: all actions are available immediately for advanced users.
- **Dual language**: AZ / EN toggle affects labels and sample explanation content.
- **Persistent local state**: theme, language, mode, and recent links are stored in `localStorage`.
- **Three-panel workspace**:
  - Left: problem, sources, progress
  - Center: session feed, action buttons, solution panel, reasoning feedback
  - Right: stats, recent history, similar practice prompts

## Suggested real backend contract
When this UI becomes a live product, these are sensible endpoints:

### `POST /api/analyze`
Input:
```json
{ "url": "https://codeforces.com/problemset/problem/1352/C", "language": "az" }
```
Output:
```json
{
  "problem": {
    "title": "1352C — K-th Not Divisible by n",
    "difficulty": 1100,
    "contest": "Codeforces Round 640",
    "tags": ["math", "implementation"]
  },
  "sources": [
    { "kind": "official", "confidence": 0.92, "summary": "..." },
    { "kind": "community", "confidence": 0.73, "summary": "..." },
    { "kind": "reconstructed", "confidence": 0.68, "summary": "..." }
  ],
  "session_id": "sess_..."
}
```

### `POST /api/session/:id/open-step`
Input:
```json
{ "step": "hint1", "mode": "guided", "language": "az" }
```
Output:
```json
{
  "title": "Hint 1",
  "content": "...",
  "newly_unlocked": ["hint2"],
  "spoiler_level": "minimal"
}
```

### `POST /api/session/:id/check-idea`
Input:
```json
{ "text": "I think I should brute force until I hit k values...", "language": "en" }
```
Output:
```json
{
  "feedback": "Brute force will be too slow. Try to see the repeating block structure..."
}
```

## Real product states to support
- loading
- source parsing failed
- official tutorial missing
- only community explanation available
- explanation reconstructed from model reasoning
- code locked / unlocked
- previous session reopened

## Design tokens
- Dark default with optional light theme
- Rounded glass cards
- Three hierarchy levels: page shell, panel, card
- Accent pair: blue + violet
- Primary font: system sans stack for portability

## Good next build step
Convert the prototype into a Next.js app with:
- `/` landing + workspace
- `/session/[id]` persisted sessions
- server route for page fetch + summarization
- optional auth and user history
