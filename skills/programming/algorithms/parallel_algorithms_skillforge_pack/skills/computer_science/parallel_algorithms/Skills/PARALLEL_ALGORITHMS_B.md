# Parallel Algorithms — Skills Lane (B)

*Generated: 2026-03-05*

## Scope
Core models, patterns, and decision procedures for designing and analyzing parallel algorithms (shared-memory + message-passing concepts).

## Key Models (quick definitions)

- **Work (T1):** total operations in the best serial schedule.
- **Span (T∞):** critical-path length (best possible with infinite processors).
- **Parallelism:** T1 / T∞ (upper bound on speedup).
- **Strong scaling:** fixed problem size, increase processors.
- **Weak scaling:** increase problem size with processors.
- **Efficiency:** speedup / P.

## Patterns (42)

### PA-PAT-001 — Parallel Divide-and-Conquer
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-002 — Parallel Reduction Tree
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-003 — Prefix Scan (Inclusive)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-004 — Prefix Scan (Exclusive)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-005 — Work Partition by Blocks
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-006 — Work Stealing for Load Balance
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-007 — Pipeline Parallelism
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-008 — Bulk Synchronous Step
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-009 — Map-Then-Reduce
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-010 — Fork-Join with Cutoff
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-011 — Wavefront / Diagonal Sweep
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-012 — Task Graph Scheduling
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-013 — Data Decomposition (1D)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-014 — Data Decomposition (2D)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-015 — Owner-Computes Rule
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-016 — Ghost Cells / Halo Exchange
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-017 — Overlap Comm with Compute
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-018 — Minimize Synchronization
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-019 — Barrier-Free (Atomic) Accumulation
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-020 — Lock Striping
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-021 — Chunked Dynamic Scheduling
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-022 — Guided Self-Scheduling
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-023 — Static Cyclic Scheduling
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-024 — Tree-Based Broadcast
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-025 — Tree-Based Gather
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-026 — All-Reduce Pattern
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-027 — Bitonic / Network Sort Skeleton
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-028 — Parallel BFS Frontier
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-029 — Parallel Dijkstra (Δ-stepping idea)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-030 — Parallel DP via Scanlines
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-031 — Speculative Parallelism (Validate/Repair)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-032 — Deterministic Reduction (Stable Order)
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-033 — Randomized Work Distribution
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-034 — Cache-Friendly Tiling
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-035 — NUMA-Aware Placement
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-036 — PRAM CREW Simulation Skeleton
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-037 — PRAM CRCW Conflict Resolution
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-038 — Critical Path (Span) Minimization
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-039 — Latency Hiding via Batching
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-040 — Granularity Control via Adaptive Cutoff
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-041 — Idempotent Retriable Tasks
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.

### PA-PAT-042 — Checkpoint/Restart for Long Runs
**Intent:** Expose parallelism while controlling overhead (sync, communication, scheduling).
**Use when:** you can split the work into independent chunks and the merge step is well-defined.
**How:**
1. Identify the independent subproblems.
2. Choose a grain size (cutoff) so overhead stays small vs useful work.
3. Execute in parallel (tasks/threads/processes) and merge with a safe reduction/compose step.
**Pitfalls:** too-fine tasks, hidden shared state, non-associative merges, false sharing.
**Check:** result matches serial; span decreases as P increases until overhead dominates.


## Action Patterns (18)

### PA-AP-001 — Estimate Speedup with Amdahl
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-002 — Estimate Speedup with Gustafson
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-003 — Compute Efficiency + Strong/Weak Scaling
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-004 — Work–Span Model Quick Analysis
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-005 — Choose Cutoff for Fork-Join
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-006 — Select Scheduling Policy (static vs dynamic)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-007 — Pick Communication Primitive (bcast/gather/allreduce)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-008 — Design a Safe Reduction (associative op check)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-009 — Avoid False Sharing Checklist
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-010 — Choose Tile Sizes (cache + vector friendly)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-011 — Barrier Placement Review
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-012 — Atomic vs Lock Decision
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-013 — Detect & Fix Load Imbalance
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-014 — Reason About Contention Hotspots
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-015 — Deadlock Avoidance (ordering)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-016 — Prove Determinism (same result every run)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-017 — Measure Overhead (timers + counters)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.

### PA-AP-018 — Scale Test Plan (N, P grid)
**Goal:** A repeatable decision or micro-procedure you can run in minutes.
**Steps:** (1) write assumptions, (2) compute/decide, (3) record 1 test you’ll run to confirm.
**Output:** a number or a single decision + a quick validation step.


## Variants (11)

- **PA-VAR-001**: Reduction: pairwise vs k-ary tree

- **PA-VAR-002**: Scan: Blelloch vs Hillis–Steele

- **PA-VAR-003**: Scheduling: guided vs work stealing

- **PA-VAR-004**: Decomposition: block vs cyclic

- **PA-VAR-005**: Communication: ring vs tree allreduce

- **PA-VAR-006**: Synchronization: barrier vs phaser

- **PA-VAR-007**: Memory: AoS vs SoA for cache

- **PA-VAR-008**: Locks: mutex vs RWLock

- **PA-VAR-009**: Atomics: fetch-add vs striped counters

- **PA-VAR-010**: Granularity: fixed vs adaptive cutoff

- **PA-VAR-011**: Fault tolerance: checkpoint vs replication


## Drills (27)

### PA-DRILL-001 — Scan: hand-run 8-element inclusive
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-002 — Reduction: compute work/span for n=16
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-003 — Amdahl: speedup for f=0.9 at P=32
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-004 — Gustafson: scaled speedup for f=0.95 at P=64
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-005 — Schedule: compare static vs dynamic on skewed loads
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-006 — Race check: identify shared variables in pseudo-code
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-007 — Barrier check: move a barrier earlier/later—what breaks?
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-008 — Chunking: pick chunk size for N=1e6, P=8
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-009 — Allreduce: draw tree for P=8
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-010 — Halo: compute bytes exchanged for 2D grid
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-011 — Tiling: choose tile for cache size C
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-012 — False sharing: spot it in an array-of-structs layout
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-013 — Work stealing: simulate deque operations on a trace
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-014 — Pipeline: compute throughput/latency for 4 stages
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-015 — BFS frontier: partition and merge strategy
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-016 — Determinism: reorder reduction—when does it change?
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-017 — Atomic vs lock: choose for counter updates
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-018 — Critical path: find span in a small DAG
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-019 — PRAM: classify algorithm as EREW/CREW/CRCW
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-020 — CRCW: resolve write conflicts (priority/combining)
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-021 — Latency hiding: batch messages—estimate savings
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-022 — Granularity: adapt cutoff across recursion depths
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-023 — Contention: model hotspots with simple queues
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-024 — NUMA: place threads/memory for 2 sockets
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-025 — Speedup curve: sketch expected vs observed
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-026 — Debug: reproduce nondeterministic bug plan
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.

### PA-DRILL-027 — Checkpoint: pick interval given failure rate
**Do:** Short exercise; verify with a one-line check.
**Done when:** you can state the answer *and* the invariant/check that confirms it.


## Cross-links
- Teaching lane: see `../Teaching/PARALLEL_ALGORITHMS_A.md`
- Index: see `../INDEX.md`
