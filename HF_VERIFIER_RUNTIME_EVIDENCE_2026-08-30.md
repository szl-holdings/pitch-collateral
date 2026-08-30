# Governed receipt verifier runtime evidence

**Observed:** 2026-08-30T01:55Z–01:57Z  
**Surface:** `SZLHOLDINGS/governed-receipt-verifier`  
**Truth boundary:** immutable public readback and executed verifier behavior; not build provenance, availability, certification, or customer usage.

## Revision identity

| Evidence | Exact value |
|---|---|
| Hugging Face Space head | `59cfd859608c22925a1161967217a4338779d006` |
| Deployed artifact base before provenance overlay | `a3be946edb5ac614eff0c9ce32e50e640c17e19e` |
| Canonical GitHub source | `szl-holdings/governed-receipt-spec` |
| Canonical signed source revision | `7d5976f089bec8af95aec915a7485d8091253190` |
| Live `verify.py` Git blob / ETag | `9ca58fdb27f6f668290e31bd32bed0159b238bdb` |
| Live `verify.py` length | `23,462` bytes |
| Live/source SHA-256 | `bd7cc88b32e4f0590cf4be7a695452ef327aa4d082c98effaf0f0c78dd20072f` |
| Byte comparison | Exact equality: `True` |

## Serving witness

- Canonical static host: `https://szlholdings-governed-receipt-verifier.static.hf.space/`
- `index.html`: HTTP 200.
- `verify.py`: HTTP 200.
- `X-Repo-Commit`: `59cfd859608c22925a1161967217a4338779d006`.
- Source-binding state: `MEASURED_VERIFY_PY_BYTE_PARITY`.
- Verification state: `STRUCTURAL_AND_FILE_HASH`.
- Build provenance: explicitly `NOT_CLAIMED`.
- Current self-referential Hub commit in the static manifest: explicitly `NOT_EMBEDDED`.

## Executed live behavior

The exact deployed `verify.py` bytes were executed in isolated Python memory against the live schema and public fixtures:

| Case | Result | Expected |
|---|---|---|
| Empty receipt list | `False` | Fail closed |
| Unsupported `{}` record | `False` | Fail closed |
| Valid genesis receipt | `True` | Pass |
| Valid five-receipt chain | `True` | Pass |
| Tampered receipt | `False` | Fail closed |

## Limits

- This proves the observed public bytes and test cases at the stated revision and time.
- It does not prove continuous availability, persistence, customer deployment, complete cryptographic trust, compliance, or absence of other defects.
- Future Space revisions require a fresh byte comparison and behavioral witness.
