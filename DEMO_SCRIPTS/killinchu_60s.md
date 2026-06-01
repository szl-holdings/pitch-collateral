# killinchu — 60-Second Live Demo Script

**Surface:** `https://szlholdings-killinchu.hf.space/globe`
**Goal:** Show the defense vertical: a Cesium globe, a drone, a geofence check, and a **signed
mission plan** — with `LEGAL_BOUNDARIES` visible.
**Doctrine v11 · "We sense, we evidence; we do not jack into third-party drones."**

---

**[0:00–0:10] — Open the globe**
> "This is killinchu — our counter-UAS defense vertical. Quechua for kestrel. It runs on the exact
> same proven substrate as a11oy."

*Action:* Open `/globe`. Cesium globe loads with the live Doctrine v11 chip and the
`LEGAL_BOUNDARIES` panel. Read the boundary line aloud:
> "Right here, on screen: we sense, we evidence — we do not jack into third-party drones. That
> posture is a feature, not a limitation."

**[0:10–0:25] — Click a drone / decode real signal**
> "Let me pick a track. This isn't a cartoon — we decode real ADS-B and MAVLink bytes."

*Action:* Click a drone; show the decoded ICAO / callsign (e.g., ICAO `4840D6`, callsign `KLM1023`).
Note the honesty label: positions are deterministic SIMULATED; geofence is a static snapshot.

**[0:25–0:42] — Run a geofence check**
> "Now a geofence containment check — real nautical-mile math."

*Action:*
```
curl -s https://szlholdings-killinchu.hf.space/api/killinchu/v2/geofence/check \
  -H 'Content-Type: application/json' -d '{"lat":32.733,"lon":-117.19}'
# => located KSAN at 0.173 nm
```

**[0:42–0:55] — Sign a mission plan**
> "And here's the part procurement cares about — every mission plan goes through the PURIQ formula
> and the 13-axis Yuyay gate, then gets signed."

*Action:*
```
curl -s https://szlholdings-killinchu.hf.space/api/killinchu/v2/mission/plan \
  -H 'Content-Type: application/json' -d '{"objective":"perimeter-watch","zone":"KSAN"}'
```
Point to the signed mission plan + DSSE receipt.

**[0:55–1:00] — Close**
> "Airgap-deployable via UDS, every decision signed and replayable. That's what an IL-4 environment
> needs."

---
*Signed Yachay `<yachay@szlholdings.dev>` · Co-Authored-By: Perplexity Computer Agent*
