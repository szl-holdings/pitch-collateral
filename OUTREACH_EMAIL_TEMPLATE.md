# Cold Outreach Email Template (Design Partner)

**SZL Holdings** · Customizable 5-paragraph template. Replace `[bracketed]` fields per target.
Keep it honest and short. Founder reviews before sending.

---

**Subject:** `[First name]` — a Lean-proven governance gate for your AI agents

---

Hi `[First name]`,

**[Para 1 — Hook]** I'm Stephen Lutar, founder of SZL Holdings. We build the missing layer beneath
agentic AI: a **formally-verified governance gate**. Not a claim — a Lean 4 proof on disk (749
declarations; we even publish that the central uniqueness result is still a conjecture, because
honesty is the product). I'm reaching out because `[specific reason this target cares — e.g., "your
team is shipping agent actions on money movement and needs gates you can actually prove"]`.

**[Para 2 — Product, vertical-specific]** For `[their context]`, that means `[a11oy: a deny-by-default
gate + 16-tool MCP server / killinchu: counter-UAS with signed mission plans / rosie: a personal
aide that signs and replays every action]`. Every governed action is wrapped in a DSSE-signed
receipt and chained into a tamper-evident ledger you can replay offline — and it's airgap-deployable
via UDS for disconnected environments.

**[Para 3 — Proof]** This isn't a deck. The five flagships are live and you can verify them right
now: `curl https://szlholdings-a11oy.hf.space/healthz` returns the honest Doctrine v11 numbers, and
`/khipu/sign` → `/khipu/verify` round-trips a real ECDSA-P256 receipt. It's open and cited — DOI
[10.5281/zenodo.20434308](https://doi.org/10.5281/zenodo.20434308), ORCID 0009-0001-0110-4173 — and
our full compliance posture (SOC 2 roadmap, security questionnaire, DPA) is public at
github.com/szl-holdings/compliance-posture.

**[Para 4 — Ask]** I'd love **30 minutes** to show you a live demo and explore whether a design-partner
pilot makes sense for `[their team]`. We're selecting a small number of design partners now, ahead of
our Series A. `[Optional warm reference: "Andrew Greene at Defense Unicorns can speak to the
collaboration."]`

**[Para 5 — CTA]** Are you open to a short call in the next two weeks? Here's my calendar:
`[calendar link placeholder]` — or reply with a couple of times that work and I'll send an invite.

Best,
Stephen Paul Lutar Jr.
Founder, SZL Holdings · stephen@szlholdings.com
huggingface.co/SZLHOLDINGS · github.com/szl-holdings · ORCID 0009-0001-0110-4173

---

## Customization cheat-sheet

| Field | Defense | Enterprise governance | Personal AI |
|-------|---------|-----------------------|-------------|
| Para 1 hook | mission autonomy needs audit | agent actions need provable gates | aide actions need provenance |
| Para 2 product | killinchu signed mission plans | a11oy deny-by-default gate + MCP | rosie sign + replay aide actions |
| Para 4 reference | "Andrew Greene / Defense Unicorns" | (founder network) | (founder network) |

**Do not** overstate: no SOC 2 yet (roadmap link instead), SLSA L1 not L3, 1 FTE. Honesty converts
better with technical buyers and avoids claim disputes later.

*Signed Yachay `<yachay@szlholdings.dev>` · Co-Authored-By: Perplexity Computer Agent*
