# Structure Survey Recovery Rules

- Never mutate an accepted canonical run in place.
- Preserve interrupted and corrupt runs with an explicit disposition.
- A resumed run must prove the previous accepted JSON hash is unchanged.
- Final acceptance requires every target slot to be full, readable, and coordinate-correct.
- Partial pregenerator completion cannot be normalized into a full denominator.

