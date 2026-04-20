# Supercars Integration Fixes & Enhancements

This implementation plan addresses the current issues with the Supercars Home Assistant integration, specifically regarding incorrect standings data and broken schedule sensors.

## Problem Statement

1. **Incorrect Standings & Results:** The `sensor.supercars_driver_standings`, `team_standings`, and `latest_results` are currently displaying incorrect, dummy data. This is because `supercars.com` is a dynamic single-page application (SPA) and does not expose this data in standard HTML or a public JSON API that `aiohttp` can easily parse.
2. **Unavailable Schedule Sensors:** The `next_practice`, `next_qualifying`, `next_race`, and `next_session` sensors are showing as unavailable. The integration was attempting to scrape a specific news article URL for the Tasmania schedule that no longer exists or lacks the expected markdown tables. 
3. **Missing Next Event:** The integration needs to accurately grab the track schedule for the next event (Tasmania Super 440). Specifically, the next practice session is scheduled for **22 May 2026 at 4:05pm AEST**.

## User Review Required

> [!WARNING]
> Because `supercars.com` actively hides its API and uses heavy JavaScript rendering, building a reliable web scraper purely in Home Assistant (Python `aiohttp`) is highly prone to breaking. Please review the proposed solutions below and let me know how you would like to proceed.

## Proposed Changes

### 1. Reliable Schedule Architecture
Instead of relying on fragile web scraping of news articles for the session schedule, we will move to a local, structured schedule file.

- **[NEW] `schedule_2026.json`:** Create a local JSON file within the `custom_components/supercars` directory. This will house the complete schedule for upcoming events.
- **[MODIFY] `schedule_coordinator.py`:** Update the coordinator to read from this local JSON file instead of fetching from the web.
- **Tasmania Schedule:** I will manually seed the JSON file with the Tasmania Super 440 schedule, ensuring `next_practice` explicitly triggers for **22 May 2026 at 4:05pm AEST**.

### 2. Standings & Results Architecture
Since native scraping is unreliable, we have a few options for fixing the incorrect standings data. **Please let me know which option you prefer:**

- **Option A (Local Managed File):** Similar to the schedule, we create a `standings.json` file that you can manually update after race weekends. The integration reads this file instantly. Reliable, but manual.
- **Option B (Reverse Engineer API):** I can write a Python script to attempt to reverse-engineer the specific GraphQL or hidden API endpoints used by the Supercars frontend. If found, we can hardcode this API endpoint. *(Note: This may still break if they change their API keys/structure).*
- **Option C (Natsoft Fallback):** We use the existing `NatsoftCoordinator` (which works for live timing) to pull the final results of the session, though this won't provide overarching Championship Standings.

## Verification Plan

### Automated Tests
- N/A for custom components, but code will be validated against Home Assistant component rules.

### Manual Verification
- After implementation, the `next_session` sensor should immediately populate with "Practice 1" and start counting down to May 22, 2026.
- The Standings sensors will display correct data based on the chosen architectural option above.
