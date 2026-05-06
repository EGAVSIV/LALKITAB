from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from datetime import datetime

import pytz

# =========================
# GEOLOCATOR
# =========================

geolocator = Nominatim(
    user_agent="lal_kitab_ai"
)

tf = TimezoneFinder()

# =========================
# GET LOCATION DATA
# =========================

def get_location_data(place):

    # =========================
    # LOCATION SEARCH
    # =========================

    location = geolocator.geocode(
        place
    )

    if location is None:

        raise Exception(
            "Location not found."
        )

    lat = location.latitude

    lon = location.longitude

    # =========================
    # FIND TIMEZONE
    # =========================

    timezone_str = tf.timezone_at(
        lat=lat,
        lng=lon
    )

    if timezone_str is None:

        timezone_hours = 0

    else:

        timezone = pytz.timezone(
            timezone_str
        )

        now = datetime.now(
            timezone
        )

        offset = now.utcoffset()

        timezone_hours = (
            offset.total_seconds() / 3600
        )

    # =========================
    # RETURN
    # =========================

    return {

        "latitude": lat,

        "longitude": lon,

        "timezone": timezone_hours
    }
