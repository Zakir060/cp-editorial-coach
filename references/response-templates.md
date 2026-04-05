# Response Templates

Use these compact templates to keep the interaction consistent.

## First response after opening a problem link

### Azerbaijani

`Dil: [AZ] [EN]`

`Seçimlər: [Hint 1] [Hint 2] [Approach] [Full Explanation] [C++ Solution]`

Then add one short sentence that confirms you understood the problem's core challenge without revealing the full method.

### English

`Language: [AZ] [EN]`

`Options: [Hint 1] [Hint 2] [Approach] [Full Explanation] [C++ Solution]`

Then add one short sentence that confirms you understood the problem's core challenge without revealing the full method.

## Hint 1

### Azerbaijani

Use this shape:

- `Hint 1:` one small directional nudge
- `Nəyə bax:` one constraint or pattern to inspect
- `Sonra:` short next-step menu

### English

Use this shape:

- `Hint 1:` one small directional nudge
- `Inspect:` one constraint or pattern to inspect
- `Next:` short next-step menu

## Hint 2

### Azerbaijani

Use this shape:

- `Hint 2:` stronger nudge
- `Əsas müşahidə:` key observation
- `Diqqət et:` one common trap
- `Sonra:` next-step menu

### English

Use this shape:

- `Hint 2:` stronger nudge
- `Key observation:` key observation
- `Watch out:` one common trap
- `Next:` next-step menu

## Approach

### Azerbaijani

Use this shape:

- `Yanaşma:` 2 to 5 short steps
- `Niyə uyğundur:` constraint fit
- `Sonra:` `[Full Explanation] [C++ Solution] [Complexity]`

### English

Use this shape:

- `Approach:` 2 to 5 short steps
- `Why it fits:` constraint fit
- `Next:` `[Full Explanation] [C++ Solution] [Complexity]`

## Full explanation

### Azerbaijani

Use these sections in this order:

1. `İntuisiya`
2. `Əsas fikir`
3. `Niyə işləyir`
4. `Reallaşdırma planı`
5. `Sonra:` next-step menu

### English

Use these sections in this order:

1. `Intuition`
2. `Core idea`
3. `Why it works`
4. `Implementation plan`
5. `Next:` next-step menu

## C++ solution

Always use this sequence:

1. one sentence telling the user this is the final contest-style implementation
2. code block with c++
3. `Time:`
4. `Space:`
5. one-line note about the trickiest implementation detail
6. next-step menu with `[Explain This Line] [Edge Cases] [Similar Problems]`

## Explain this line

When the user highlights one sentence, formula, or code block:

1. restate the exact part in simpler words
2. explain what each symbol or phrase refers to
3. connect it back to the main invariant or state
4. end with one quick check question only if it materially helps
