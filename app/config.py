"""Configuration. There is NO global API key anymore — every user brings their
own, stored encrypted in the DB (see crypto.py). Only paths + cadence here."""
import os
from pathlib import Path

BASE_URL = "https://wdgwars.pl"
USER_AGENT = "warroom-companion/0.1 (+https://warroom.mechanics-toolbox.org)"

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.environ.get("WARROOM_DATA", ROOT / "data"))
DB_PATH = DATA_DIR / "warroom.sqlite"
MASTER_KEY_PATH = DATA_DIR / "master.key"

# Cap on new sign-ups (each user = 1 third-party API key in our custody +
# poll load) — deliberately start small, raisable via env without a rebuild.
MAX_USERS = int(os.environ.get("WARROOM_MAX_USERS", "30"))
CONTACT_MAIL = "st4bleground@proton.me"

# Display timezone: SQLite stores UTC, the UI shows wall-clock time of this zone.
TZ = os.environ.get("WARROOM_TZ", "Europe/Berlin")

# member-territories is only recomputed server-side every 5 min via cron.
POLL_SECONDS = 300
# Concurrent per-user poll workers. Deliberately small: this caps how many
# simultaneous requests we send to the wdgwars API (be a good citizen).
POLL_WORKERS = int(os.environ.get("WARROOM_POLL_WORKERS", "4"))
REINFORCE_BUFFER = 3
# Turf = own AP cells + ring of TURF_RING cells around them (Chebyshev).
# 4 cells ≈ 6–9 km at ~50°N (0.02° ≈ 2.2 km lat / ~1.4 km lng).
TURF_RING = 4
# Background road-snap budget per poll cycle: how many not-yet-classified virgin
# cells get checked against Overpass (8 cells/query → 48 = 6 queries per 5 min,
# ~1.7k queries/day worst case — well within Overpass fair use). Water/forest
# results are cached forever, so this converges: a few thousand cells are fully
# classified within a day, then only freshly appearing ring cells trickle in.
ROAD_DRIP = int(os.environ.get("WARROOM_ROAD_DRIP", "48"))
