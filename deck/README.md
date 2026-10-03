# Investor diligence deck

**Evidence class:** DECLARED internal diligence draft  
**Circulation:** NOT FOR EXTERNAL CIRCULATION  
**Evidence snapshot:** 2026-08-30  
**Authority routing reviewed:** 2026-09-22  
**Protected source base:** `20cd4537effa28bacda8ef832e2a720b852c98d7`

`SZL_Investor_Deck_2026-08-30.pptx` is an editable, 11-slide working deck for bounded investor diligence. It is not a current runtime report or a Series A claim. Before external use, select one buyer segment and reconcile founder-approved financing terms, hiring, use of funds, and runway to a 12–18 month operating model.

## Authority and evidence boundary

- Product and runtime originate at `a-11-oy.com`.
- The interactive verifier remains at `a-11-oy.com/verify`.
- Proof, RECORD, evaluations, known bounds, and investor diligence originate at `a11oy.net`.
- The Hugging Face governed-verifier witness and A11oy `/verify` are separate evidence surfaces.
- Source, artifact, deployment, runtime, evaluation, and authorization are distinct.
- Reachability provides no production proof.
- Unconditional Lambda uniqueness remains Conjecture 1.
- Killinchu effectors remain SIMULATED.
- The deck asserts no customer, revenue, paid pilot, partnership, production deployment, held certification, TAM, ARR, valuation, or pricing result.

Every slide contains a `[Sources]` speaker-note block with immutable GitHub blob URLs. `MANIFEST.sha256` binds the exact reviewed deck bytes. The protected Git history and hosted checks provide surrounding provenance; the manifest alone is not an author signature.

## Verify

From the repository root:

```text
python -I -B deck/check_deck.py
```

The checker fails closed on a hash mismatch, unsafe or malformed OOXML, the wrong slide or note topology, missing exact-revision source blocks, stale authority URLs, non-doctrinal evidence-table states, unsupported affirmative claims, macros, embedded objects, or missing doctrine boundaries. Permitted evidence classes are not required when no qualifying evidence exists; in particular, the deck does not claim a fresh MEASURED result.

The checker does not establish visual quality, current public/provider state, source-to-runtime identity, customer or revenue status, compliance, production readiness, or the truth of a sentence merely because it appears in the file. Visual QA and exact-time investor-demo preflight remain separate requirements.

## Editing procedure

1. Update the canonical Markdown evidence first.
2. Regenerate or edit the PowerPoint using the approved presentation toolchain.
3. Render and inspect every slide at full size.
4. Run the package, layout, and repository integrity checks.
5. Recompute `MANIFEST.sha256` only after the final deck bytes are fixed.
6. Review the manifest change together with the binary change.

Rendered PNGs, montages, inspection NDJSON, and validation receipts are local QA outputs unless the repository explicitly adopts them as versioned evidence.
