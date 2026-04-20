# Supercars Championship — Home Assistant Integration

A Home Assistant custom integration that pulls live timing data from the Natsoft V8 Supercars feed, giving you real-time race sensors, automations, and a dashboard card.

## Features

- 🏁 **Live flag state** — green, yellow, safety car, VSC, red, chequered
- 🏆 **Race leader** — driver name, car number, team
- 🔢 **Lap counter** — current lap / total laps
- ⏱ **Time remaining** in session
- 🌡 **Track conditions** — air & track temperature
- 📡 **Auto-adjusting poll rate** — 5 s when live, 60 s when idle
- 🎙 **At-circuit stream link** — surfaces supercars.fm when a session is active *(geo-locked, works at the venue)*

## Installation (HACS)

1. In HACS → Integrations → ⋮ → Custom repositories
2. Add `https://github.com/yourusername/ha-supercars` as **Integration**
3. Install **Supercars Championship**
4. Restart Home Assistant
5. Settings → Integrations → Add → **Supercars Championship**

## Sensors Created

| Entity | Description |
|--------|-------------|
| `sensor.supercars_flag_state` | Current flag / session state |
| `sensor.supercars_race_leader` | Leading driver |
| `sensor.supercars_current_lap` | Current lap number |
| `sensor.supercars_session` | Session name (Race 1, Qualifying, etc.) |
| `sensor.supercars_round` | Round / circuit name |
| `sensor.supercars_time_remaining` | Session time remaining |
| `sensor.supercars_air_temperature` | Air temp (°C) |
| `sensor.supercars_track_temperature` | Track temp (°C) |

## Dashboard

Copy `lovelace_card.yaml` into your dashboard. Requires:
- [mushroom-cards](https://github.com/piitaya/lovelace-mushroom)
- [button-card](https://github.com/custom-cards/button-card)

## Automations

See `automations_example.yaml` for ready-to-use automations:
- Safety car alert
- Red flag alert
- Lead change notification
- Session start/end notification

## Data Source

Live timing data is sourced from the publicly accessible Natsoft timing server at `server.natsoft.com.au:8080/LiveMeeting/V8SUPER`.

The at-circuit audio stream link points to [supercars.fm](https://supercars.fm), which is geo-locked to the race venue and available to attendees on-site.
