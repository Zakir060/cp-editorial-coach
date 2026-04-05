# CP Editorial Coach UI Spec

## Product summary
A learning-first interface for competitive programming users who paste a problem link and want controlled help, not instant spoilers.

## Core screens
### 1. Top bar
- Brand block
- Theme toggle
- Language switch (AZ / EN)

### 2. Hero / intake block
- Problem link input
- Analyze button
- Guided mode / Fast track toggle
- Demo session button
- Parsing status line

### 3. Left panel
- Current problem card
- Ranked source cards
- Unlock progress card

### 4. Center panel
- Session feed with coach messages
- Action grid for progressive help
- C++ solution panel
- "Check my reasoning" area

### 5. Right panel
- Session stats
- Recent links
- Similar practice directions

## Unlock sequence
Guided mode opens help in this order:
1. Hint 1
2. Hint 2
3. Approach
4. Full Explanation
5. Why It Works
6. Complexity
7. Edge Cases
8. Simplified Editorial
9. Similar Problems
10. C++ Solution

Fast track makes every action available immediately.

## Interaction rules
- The session starts only after link analysis or demo load.
- Every opened step is appended to the feed.
- Unlock state and recent links persist in local storage.
- The code panel stays hidden in practice terms until `C++ Solution` is opened.
- Language switch re-renders UI labels and example content.

## Visual direction
- Dark glassmorphism by default
- Large rounded cards
- Blue/violet gradient for primary actions
- Dense but readable information layout
- Fully responsive under 1200px and 920px breakpoints

## Recommended next engineering step
Implement this prototype as a Next.js app with real source retrieval and server-side session state.
