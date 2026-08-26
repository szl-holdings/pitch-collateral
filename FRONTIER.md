# Frontier thesis — proof-carrying governed execution

SZL's technical thesis is that consequential AI actions should carry enough evidence to reconstruct what policy admitted them, what source and artifact ran, which inputs governed the action, and what the system refused.

## Architecture

- policy admission before execution;
- bounded execution with explicit uncertainty and refusal states;
- structured receipts and post-action verification;
- source, artifact, deployment, and served-revision identity;
- reusable governance primitives demonstrated through focused applications.

## Formal-methods boundary

Lean 4 supports specified kernel properties at exact revisions and under documented assumptions. Conditional Theorem U and bounded kernel results must be described separately from unconditional Lambda uniqueness, which remains Conjecture 1. These results do not prove that a model is correct, that every action is safe, or that the platform is formally verified.

## Commercial wedge

The initial hypothesis is a governed workflow owned by a technical-risk buyer in a regulated, safety-critical, or operational setting. A11oy is the primary prototype; Killinchu is a vertical demonstration. Selection of the first buyer and workflow requires customer evidence.

## Competitive standard

Compare alternatives through a dated capability matrix: policy admission, receipt schema, artifact identity, deployment identity, persistence, verification, integration effort, and operational controls. Do not use exclusivity claims without reproducible evidence.

## Product gate

A capability becomes investor-promoted only when its source, tests, artifact, deployment, served revision, runtime behavior, and limitations are recorded in the evidence register. A receipt is evidence, not a certification or safety guarantee.
