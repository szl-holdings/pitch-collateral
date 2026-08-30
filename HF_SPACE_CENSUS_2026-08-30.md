# Public Hugging Face Space census — 2026-08-30

**Evidence state:** public inventory observed; canonical-host reachability
witnessed  
**Organization:** `SZLHOLDINGS`

## Scope and method

At `2026-08-30T11:55:26.9810525Z`, the unauthenticated public author query
<https://huggingface.co/api/spaces?author=SZLHOLDINGS&limit=100> returned six
Spaces. At `2026-08-30T11:56:06.1293247Z`, each public Space API record was
read separately to capture its exact revision, SDK, and runtime state. Between
`2026-08-30T11:58:40Z` and `2026-08-30T11:58:43Z`, an unauthenticated `GET`
was issued to each API-derived canonical serving root.

No token, private inventory, provider setting, or deployment mutation was used.

## API census

| Space | SDK | Exact revision | API runtime | Compute / replicas observed |
|---|---|---|---|---|
| [`SZLHOLDINGS/a11oy`](https://huggingface.co/spaces/SZLHOLDINGS/a11oy/tree/45b33a24c1dd3891a47f2c31174fd425fb3a445d) | Docker | `45b33a24c1dd3891a47f2c31174fd425fb3a445d` | `RUNNING` | `cpu-basic`; 1/1 |
| [`SZLHOLDINGS/immune`](https://huggingface.co/spaces/SZLHOLDINGS/immune/tree/c85d490052b68ebd1c9c9d3ef7792410ad8cee5a) | Docker | `c85d490052b68ebd1c9c9d3ef7792410ad8cee5a` | `RUNNING` | `cpu-basic`; 1/1 |
| [`SZLHOLDINGS/killinchu`](https://huggingface.co/spaces/SZLHOLDINGS/killinchu/tree/3249936052bc9d8a7353b32c7dbf3fccbf0d37bf) | Docker | `3249936052bc9d8a7353b32c7dbf3fccbf0d37bf` | `RUNNING` | `cpu-basic`; 1/1 |
| [`SZLHOLDINGS/szl-khipu`](https://huggingface.co/spaces/SZLHOLDINGS/szl-khipu/tree/3af5fda4b810fc1d62847b173db3bf8caea8f42d) | Docker | `3af5fda4b810fc1d62847b173db3bf8caea8f42d` | `RUNNING` | `cpu-basic`; 1/1 |
| [`SZLHOLDINGS/governed-receipt-verifier`](https://huggingface.co/spaces/SZLHOLDINGS/governed-receipt-verifier/tree/59cfd859608c22925a1161967217a4338779d006) | Static | `59cfd859608c22925a1161967217a4338779d006` | `RUNNING` | static; 1/1 |
| [`SZLHOLDINGS/szl-atelier`](https://huggingface.co/spaces/SZLHOLDINGS/szl-atelier/tree/7527467d492eeb2eec5d2acca8629761a8eabcc3) | Static | `7527467d492eeb2eec5d2acca8629761a8eabcc3` | `RUNNING` | static; 1/1 |

## Canonical serving witness

| Space | API-derived serving root | Observed HTTP status |
|---|---|---|
| `a11oy` | <https://szlholdings-a11oy.hf.space/> | `200` |
| `immune` | <https://szlholdings-immune.hf.space/> | `200` |
| `killinchu` | <https://szlholdings-killinchu.hf.space/> | `200` |
| `szl-khipu` | <https://szlholdings-szl-khipu.hf.space/> | `200` |
| `governed-receipt-verifier` | <https://szlholdings-governed-receipt-verifier.static.hf.space/> | `200` |
| `szl-atelier` | <https://szlholdings-szl-atelier.static.hf.space/> | `200` |

The public author query therefore supported the bounded statement that the
organization exposed six public Spaces at the observation time: four Docker
and two static. Both static Spaces served from their API-reported
`*.static.hf.space` hosts.

The separate governed-verifier byte identity and fail-closed behavior witness
is recorded in `HF_VERIFIER_RUNTIME_EVIDENCE_2026-08-30.md`.

## Follow-up drift readback

At `2026-08-30T13:18:53.3985775Z`, the same public author query still returned
six Spaces, while the `a11oy` API record had advanced to revision
`615602b6a820655c106db6517f70260a92a170b0` with stage `RUNNING`. This later
readback does not rewrite the earlier revision-bound census. It demonstrates
that a point-in-time count can remain stable while an individual Space revision
changes, so neither snapshot should be presented as current without a fresh
readback.

## Limits

- This is a public Space census only; models, datasets, and private assets were
  not inventoried.
- `RUNNING` and HTTP `200` establish API-reported state and point-in-time public
  reachability, not availability, workflow correctness, durability, security,
  production use, or a service-level commitment.
- Revisions and runtime state can change after the observation time. Re-run the
  same API and canonical-host checks before external use.
- Except for the separately documented governed verifier, this record does not
  establish source parity, artifact attestation, build provenance, or exhaustive
  behavior.
