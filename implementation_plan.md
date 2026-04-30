# Supercars Integration Fixes & Enhancements

This implementation plan tracks fixes to the Supercars Home Assistant integration.

## Problem Statement

1. **Incorrect Standings & Results:** `sensor.supercars_driver_standings`, `team_standings`, and `latest_results` were displaying dummy data because supercars.com is a Next.js App Router SPA with no documented public API.
2. **Unavailable Schedule Sensors:** `next_practice`, `next_qualifying`, `next_race`, `next_session` were unavailable because the old scraper targeted a news article URL that no longer exists.
3. **Missing Next Event:** Tasmania Super 440 — Practice 1 is on **22 May 2026 at 4:05pm AEST**.

## Architectural Decisions

- **Schedule:** local JSON file (`schedule_2026.json`) is the source of truth; web scraping of `supercars.com/news/...` is a fallback.
- **Standings (Option B):** reverse-engineered API access. Tries speculative REST endpoints, then a Next.js RSC fetch (`RSC: 1` header) for the App Router flight payload, then HTML scraping that covers `__NEXT_DATA__`, `window.__*STATE__`, `<script type="application/json">`, and `self.__next_f.push(...)` flight chunks. Stale-cache fallback; never returns dummy data.
- **Results (Options B + C):** during a live Natsoft session, results come straight from the live timing feed (Option C). Outside sessions, the same Option B chain as standings is used.

## Status

| Area | Status |
|------|--------|
| Tasmania schedule (Practice 1 → Race 3) | Done — `schedule_2026.json` |
| `schedule_coordinator` reads local JSON first | Done |
| `standings_coordinator` Option B chain | Done |
| `results_coordinator` Option C (Natsoft live) | Done |
| `results_coordinator` Option B (idle) | Done |
| Next.js flight chunk parser (`__next_f.push`) | Done — `spa_extract.py` |
| RSC fetch fallback | Done |
| Sensor data-mutation bug (`entity_picture` leak) | Done |
| Calendar rounds 6–14 session times | **Pending** — empty `sessions: []` slots in `schedule_2026.json`; will be populated when each round's official schedule is published |

## Verification

- `next_session` populates with "Practice 1" and counts down to **22 May 2026 16:05 AEST**.
- During an active Natsoft session, `latest_results` shows live top-10 with `source: natsoft_live`.
- Outside sessions, the integration probes API → RSC → HTML in order; each layer is logged at INFO when it succeeds.
- A unit-style smoke test (`python3` against synthetic JSON + flight chunks) confirms the parser detects standings/results shapes and gracefully returns nothing on the live SPA HTML, where the data is fetched client-side.
