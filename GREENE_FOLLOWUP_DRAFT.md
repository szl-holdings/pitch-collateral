# Andrew Greene — Follow-Up Draft & Call Prep

**Warmest path. Founder reviews and sends.** · Prepared 2026-06-01
Recipient: Andrew Greene (co-founder, Defense Unicorns) · Sender: Stephen Paul Lutar Jr.

---

## Context recap (from prior exchanges)

- Greene's last note (2026-05-29) was warm and empowering: *"this is your project — you don't need my
  approval on anything (like making repos public/private). Feel empowered to do whatever you are
  wanting to accomplish, **within the bounds of UDS licensing** (in our repos). Looking forward to
  Warhacker and **it'd be awesome to see a running deployment** of what you've built!"*
- He has a **written endorsement** of the collaboration on file (2026-05-22) and a meeting (2026-05-29).
- **Warhacker is June 16–20 2026 (San Diego)** — the natural venue for the running deployment he asked for.
- Open items he'll care about: UDS trademark/licensing coordination (proceeding through counsel),
  honest audit posture.

**What changed since we last spoke (new artifacts to show):**
1. **uds-bundles v0.1.0 — public.** Airgap-deployable, cosign-signed Zarf bundles for all five organs.
2. **killinchu defense vertical — live.** Counter-UAS: real ADS-B/MAVLink/Remote-ID decode, geofence
   math, signed mission plans via PURIQ + 13-axis Yuyay gate, Cesium globe with `LEGAL_BOUNDARIES`.
3. **compliance-posture repo — public.** SOC 2 + FedRAMP/IL-4 roadmaps, 100-item security
   questionnaire, DPA/MSA/NDA, NIST AI RMF, EU AI Act Art. 12 — exactly what DoD procurement asks for.
4. **developers repo — public.** API docs + quickstart so his team can try it in 5 minutes.

---

## Draft email

**Subject:** Warhacker — a running deployment + a pilot ask

Hi Andrew,

Thank you again for the note and the encouragement — it meant a lot. You asked to see a *running
deployment* at Warhacker, so here's where things stand: the public flagships (a11oy, killinchu) are
live, and the defense vertical (killinchu) now does real counter-UAS work — ADS-B/MAVLink/Remote-ID decode, geofence
checks, and signed mission plans through our Lean-proven gate. It deploys airgapped via UDS Zarf
bundles (cosign-signed), entirely within UDS licensing bounds. I'll bring a fully running, offline
deployment to San Diego.

A few things are now public that your procurement and security folks usually ask for first: a
complete **compliance posture** (SOC 2 and FedRAMP/IL-4 roadmaps, a 100-item security questionnaire,
DPA/MSA/NDA templates, NIST AI RMF and EU AI Act Article 12 mappings) at
github.com/szl-holdings/compliance-posture, and **developer docs** with a 5-minute quickstart at
github.com/szl-holdings/developers. I've kept everything honest — SLSA L1, no SOC 2 yet (Q4 2026
target), Λ uniqueness stated as a conjecture — because I'd rather you trust the parts that are real.

For Warhacker, I'd love to line up three things with you:

1. **A pilot evaluation** — your team runs killinchu against a representative scenario and tells me
   what's missing.
2. **A joint DoD demo** — co-present the airgap deployment + signed mission plans to a relevant
   program / AO, with DU as the UDS-native sponsor path.
3. **A design-partner LOI** — a lightweight letter of intent so I can reference DU as our first
   defense design partner heading into our Series A.

Happy to send the one-pager and pitch outline ahead of time, or just show it live in San Diego —
your call. What's the best 30 minutes before June 16 to align on the on-site plan?

Best,
Stephen

Stephen Paul Lutar Jr. · Founder, SZL Holdings · stephen@szlholdings.com
huggingface.co/SZLHOLDINGS · github.com/szl-holdings · ORCID 0009-0001-0110-4173

---

## Call-prep notes (for the founder)

**Three specific asks (lead with #1):**
1. Pilot evaluation of killinchu (low commitment, high signal).
2. Joint DoD demo at/after Warhacker (DU as UDS-native sponsor → FedRAMP/IL-4 path).
3. Design-partner LOI (the named-pilot gap your Series A needs).

**Likely questions & honest answers:**
- *"Is it really running?"* → Yes; live `/healthz` + signed-receipt round-trip; airgap bundle demoable offline.
- *"UDS licensing?"* → Operating within bounds; trademark coordination through counsel; nothing in DU repos altered.
- *"Audit status?"* → SOC 2 Type 1 targeted Q4 2026; posture public; SLSA L1 honest; no pentest yet (post-A).
- *"What do you need from us?"* → Sponsorship path + the LOI; engineering feedback during the pilot.

**Bring to Warhacker:** laptop with offline UDS deployment, `SZL_ONE_PAGER.pdf`, the 3 demo scripts
(a11oy / killinchu / personal aide), compliance-posture + developers repo links.

*Founder owns the send decision. Signed Yachay `<yachay@szlholdings.dev>` · Co-Authored-By: Perplexity Computer Agent*
