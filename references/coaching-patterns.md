# Coaching Patterns

Use this file when the user is confused, stuck, or partially correct.

## Common failure modes

### Wrong invariant

Symptoms:

- the user updates an answer greedily without proving the local choice stays valid
- the explanation sounds plausible on examples but breaks on edge cases

Response pattern:

- name the hidden quantity that must stay true
- show where their update loses that property
- give the smallest fix or redirect toward the correct invariant

### Wrong dp state

Symptoms:

- the state does not contain enough information for the transition
- the user carries redundant information and gets too many states

Response pattern:

- say exactly what decision the future still depends on
- redesign the state around that dependency
- mention why anything else can be dropped

### Wrong greedy choice

Symptoms:

- the user chooses the best immediate move without an exchange argument
- tie cases break the idea

Response pattern:

- show the local decision that must be justified
- provide a tiny exchange argument or counterexample
- redirect to the correct sorted order, priority rule, or proof lens

### Complexity mismatch

Symptoms:

- the idea is logically correct but too slow for the constraints
- the user ignores preprocessing or data-structure support

Response pattern:

- quantify the slow step explicitly
- map it to the constraint bottleneck
- suggest the missing optimization layer

## Good coaching habits

- preserve the user's progress when they are partially correct
- fix one misconception at a time
- prefer one sharp counterexample over many vague warnings
- after correcting the misunderstanding, return to the spoiler ladder instead of dumping everything

## Similar-problem recommendations

When recommending practice:

- choose problems that repeat the same core insight, not just the same tags
- explain the transfer lesson in one sentence
- avoid too many recommendations at once
