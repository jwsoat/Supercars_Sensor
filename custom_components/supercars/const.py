"""Constants for the Supercars Championship integration."""

DOMAIN = "supercars"
DEFAULT_NAME = "Supercars"

# Natsoft live timing endpoint — a websocket feed, not a plain HTTP resource.
# "V8SUPER" is a standing channel name for the whole category (it does not
# change per event/round; confirmed live against the current meeting).
NATSOFT_URL = "ws://server.natsoft.com.au:8080/LiveMeeting/V8SUPER"

# How often to poll when a session is active (seconds)
SCAN_INTERVAL_ACTIVE = 5
# How often to poll when no session is detected (seconds)
SCAN_INTERVAL_IDLE = 60

# Stream link (geo-locked, for at-circuit use only)
STREAM_URL = "https://supercars.fm"
STREAM_NOTE = "Available at-circuit only"

# Session state values from Natsoft
SESSION_STATES = {
    "Green": "green_flag",
    "Yellow": "yellow_flag",
    "SafetyCar": "safety_car",
    "VSC": "virtual_safety_car",
    "Red": "red_flag",
    "Chequered": "chequered_flag",
    "Paused": "paused",
    "Inactive": "inactive",
}

# Sensor unique ID suffixes
SENSOR_SESSION = "session"
SENSOR_LEADER = "leader"
SENSOR_LAP = "lap"
SENSOR_FLAG = "flag"
SENSOR_WEATHER = "weather"

CONF_SCAN_INTERVAL = "scan_interval"
