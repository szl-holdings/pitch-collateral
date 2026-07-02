# SZL Frontier Thesis — Proof-Carrying Governed Intelligence (PCGI)
_Forge, for Rosa. Grounded in real org primitives; no fabricated capability claims._

## The one-line thesis
Turn every AI decision the org makes — a11oy orchestration steps, killinchu counter-UAS
tracks/engagement recommendations, yarqa surrogate predictions — into a **proof-carrying
artifact**: a single cryptographically-signed receipt that binds *model + input digest + output
digest + measured energy + the governance policy that gated it + a formal (Lean-checked) guarantee
about the kernel that aggregated it + optional multi-party (BFT) witnessing*. This is
"Content Credentials (C2PA) for autonomous AI decisions," but with **formal-methods teeth and
energy honesty** — a category the incumbents do not occupy.

## Why now, why lucrative (from 2026 market research)
- **EU AI Act high-risk enforcement is live (Aug 2026): fines up to €35M or 7% of global turnover.**
  Governance stopped being optional and became an infrastructure line-item. Gartner: AI-governance
  platform spend passes $1B by 2030; orgs running one are 3.4× more likely to call governance
  effective.
- **Verifiable / Trustworthy AI is the highest-growth slice (est. 34–47% CAGR)** — explainability,
  red-teaming, ZKP/TEE, formal verification. Synthetic-evidence lawsuits + provenance-missing
  content are driving demand for cryptographic "this output came from this model at this time under
  this policy" attestation (C2PA, in-toto, SLSA, cosign/Sigstore, FIDO agent-trust, TEE verifiable
  compute).
- **Defense AI (counter-UAS) is $4–8.5B in 2026 → $20–36B by 2033–35 (~22–28% CAGR).** killinchu
  plays here; the differentiator buyers now demand is *auditable, accountable* autonomy — every
  engagement decision needs a defensible evidence trail. That is literally what our receipt stack
  produces.

The incumbents (Palantir AIP, Databricks, DataRobot) do orchestration + governance dashboards. None
ship a **signed, energy-metered, formally-checked, BFT-witnessed receipt per decision.** That gap is
the moat.

## What we ALREADY have (real, in-repo — this is the unfair advantage)
- `szl-receipt` — DSSE/ECDSA-P256 signed receipts, in-toto statements, cosign-compatible. Now the
  shared home; governed-inference-meter and szl-energy-attest already delegate to it.
- `governed-inference-meter` / `szl-energy-attest` — energy-metered governed inference; **measured
  joules verbatim or honest UNAVAILABLE**, never fabricated. Honesty is enforced, not aspirational.
- `lutar-lean` / `lean-kernel` — Lean 4 + Mathlib formalization; Λ (Lambda-Spine) uniqueness proof.
  This is the "formal guarantee" leg almost nobody in the commercial provenance space has.
- `szl-lambda-gate` / `szl-governed-norm` — universal governed kernels (weighted geometric
  aggregation, RMSNorm/LayerNorm) that the Lean proofs are about.
- `khipu-consensus` / `szl-mesh` — BFT 3-of-4 multi-party-witnessed agreement; each witness signs.
  This is the "multi-party notarization" leg.
- `szl-lake` — append-only DSSE receipt store (transparency-log shaped).
- `anatomy` — a 3D-navigable governed-AI organ substrate. **This is the holo surface.**
- `a11oy` (orchestration Command Center), `killinchu` (counter-UAS), `yarqa` (signed-provenance
  plug-flow → PINN surrogate). The three decision-producers that emit receipts.

## The "holo" frontier Rosa asked for — the Covenant Cockpit
Research (2026): Avalon NOVAC true holographic table display (May 2025), neural holography, HYPERVSN
AI holographic content, EchoPixel medical holograms; light-field + volumetric encoding advancing
fast. The org already has `anatomy` — a 3D navigable substrate.

**Concept: a holographic / light-field "Covenant Cockpit"** — render the live governed-AI substrate
as a navigable 3D surface where you can *see and rotate the provenance graph of every AI decision in
real time*: organs (a11oy/killinchu/yarqa) emitting decisions → each decision a signed node → edges
to the Λ-gate that governed it, the energy it burned, the Lean proof that backs the kernel, and the
BFT witnesses that co-signed. Selecting any node pulls its DSSE receipt and verifies it live.
- Near-term, honest, shippable: WebGL/WebXR volumetric render in the a11oy Command Center driven by
  real `szl-lake` receipts (works on a normal screen today; light-field/holographic-table output is
  a hardware upgrade path, not a fabricated claim).
- This is the "no one has dreamed of" surface: a **trust cockpit you can walk around**, where the
  hologram *is* the audit trail. Defensible because it's backed by real signed evidence, not a
  data-viz skin.

## yarqa as the wedge proof (PINN + provenance)
yarqa becomes the first fully proof-carrying *scientific* surrogate: a PINN/neural-operator surrogate
(state-of-art landscape: FNO/DeepONet, NVIDIA PhysicsNeMo, FBPINN domain decomposition) for the
plug-flow/CFD compute, where **every prediction ships a receipt** with measured provenance and an
honest out-of-validated-range UNAVAILABLE instead of an extrapolated (fabricated) physical number.
This is the template every other decision-producer copies: fast surrogate + honest bounds + signed
evidence.

## Product framing (lucrative packaging)
1. **PCGI SDK** — drop-in `emit_receipt(...)` that any model/agent calls to produce the bound,
   signed, energy-metered, (optionally) Lean-anchored + BFT-witnessed receipt. Consumes szl-receipt.
2. **Covenant Ledger** — hosted append-only receipt store + verifier (szl-lake), the system of
   record for "prove this AI decision." Sells to regulated + defense buyers under EU AI Act pressure.
3. **Covenant Cockpit** — the holo/3D command surface (anatomy + a11oy) for exploring & verifying.
4. **Vertical land-and-expand:** killinchu (defense, auditable autonomy) and yarqa (verifiable
   scientific/industrial surrogates) as the two reference verticals that prove the horizontal SDK.

## Honesty guardrails (non-negotiable, already org doctrine)
- Receipt = **evidence, not conformity/certification/safety guarantee**. Never an SLSA-conformance
  claim; szl-owned predicateType only.
- Energy: measured verbatim or UNAVAILABLE. Never fabricated joules/carbon.
- Surrogates: honest error/UNAVAILABLE outside validated range. Never an extrapolated physical value
  presented as truth.
- Formal proofs cover the **kernel invariant**, not "the AI is correct." Say exactly what each proof
  does and does not establish.

## Status of this wave (real landed results — honest, verified 2026-07-02)
This wave deliberately did NOT "make every tab real" in one shot (giant single-agent
sweeps exceed a session and leave half-work). Instead it landed real, CI-verified,
doctrine-honest slices — the wedge, not the whole cliff:

- **yarqa — the wedge proof (LANDED, pushed `668071b`).** Real physics-informed
  plug-flow surrogate + a `szl_receipt`-delegated attestation layer. Bounded honesty
  enforced in code: interpolation of MEASURED anchors only, EXACT + zero-width at an
  anchor, and explicit `UNAVAILABLE` (value=None) outside the validated range — never
  an extrapolated physical number. The monotonicity prior is *checked & reported on
  the anchors*, not falsely advertised as a proof (the reduction genuinely wiggles at
  sub-anchor scale — we say so). 91 tests pass; functional CI green (Space-CI, SBOM,
  gitleaks, Receipt Sign, DCO). NOTE: the org `hf-deploy` reusable is red on this
  commit — pre-existing infra, blocked on `.github#172` + `HF_TOKEN`, unrelated to
  this code.
- **khipu-sda-core — consolidation slice (LANDED, pushed `a7fd247`, CI green).**
  `make_intoto_receipt` now delegates the in-toto Statement v1 shape to the shared
  `szl_receipt.attest.build_statement` (single source of truth) with a byte-identical
  local fallback — one more producer folded onto the canonical receipt, output
  unchanged.
- **a11oy — honesty fix (LANDED, pushed `863bd3e`, guards green).** The Compute
  Orchestration page was rendering fabricated cluster telemetry (invented nodes/jobs +
  a `Math.random()` utilization history). Replaced with explicit `UNAVAILABLE` panels
  until a real metrics source is wired. Doctrine + Overclaim Guard + drift/Dockerfile
  guards + DCO + demo-freeze all pass.
- **killinchu — classification fix (LANDED earlier, `d94be98`, CI green).** `qhawaq`
  correctly classified as a backend governance ring (Doctrine, Overclaim Guard, HF
  Sync all green).

Still open (honest): a11oy has many other tabs; killinchu's full 16-view
operationalization; a full org consolidation map. These are the next bounded slices,
not claimed done.
