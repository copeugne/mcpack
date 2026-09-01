# Atomic Density Checkpoint Policy

Each seed/pass checkpoint is published only after a clean stop and offline slot scan. Write the new run JSON atomically, hash it, and retain the previous accepted checkpoint. A failed or interrupted attempt receives a separate immutable disposition record and never replaces accepted state.

