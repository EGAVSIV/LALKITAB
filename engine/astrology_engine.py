from datetime import datetime
import swisseph as swe

from engine.planet_engine import get_planet_positions
from engine.house_engine import calculate_houses
from engine.house_engine import get_house

from engine.prediction_engine import get_prediction
from engine.remedy_engine import get_remedies

from engine.state_engine import determine_planet_state

from engine.conjunction_engine import detect_conjunctions
from engine.yoga_engine import detect_yogas

from engine.manglik_engine import is_manglik

# =========================
# JULIAN DATE
# =========================

def get_julian_day(date_str, time_str, timezone):

    dt = datetime.strptime(
        date_str + " " + time_str,
        "%Y-%m-%d %H:%M"
    )

    hour = dt.hour + dt.minute / 60.0 - timezone

    jd = swe.julday(
        dt.year,
        dt.month,
        dt.day,
        hour
    )

    return jd

# =========================
# MAIN ANALYSIS
# =========================

def analyze_chart(
    dob,
    tob,
    lat,
    lon,
    timezone
):

    jd = get_julian_day(
        dob,
        tob,
        timezone
    )

    # =========================
    # PLANET POSITIONS
    # =========================

    planet_positions = get_planet_positions(jd)

    # =========================
    # HOUSES
    # =========================

    houses, ascendant = calculate_houses(
        jd,
        lat,
        lon
    )

    # =========================
    # SUN DEGREE
    # =========================

    sun_degree = planet_positions["Sun"]

    # =========================
    # REPORT
    # =========================

    report = []

    # =========================
    # PLANET ANALYSIS
    # =========================

    for planet, degree in planet_positions.items():

        house = get_house(
            degree,
            ascendant
        )

        # =========================
        # DETERMINE STATE
        # =========================

        state = determine_planet_state(
            planet,
            degree,
            sun_degree
        )

        # =========================
        # PREDICTIONS
        # =========================

        predictions = get_prediction(
            planet,
            house,
            state
        )

        # =========================
        # REMEDIES
        # =========================

        remedies = get_remedies(
            planet,
            state
        )

        # =========================
        # MANGLIK
        # =========================

        manglik = False

        if planet == "Mars":

            manglik = is_manglik(house)

        # =========================
        # SAVE REPORT
        # =========================

        report.append({

            "planet": planet,

            "degree": degree,

            "house": house,

            "state": state,

            "predictions": predictions,

            "remedies": remedies,

            "manglik": manglik

        })

    # =========================
    # CONJUNCTIONS
    # =========================

    conjunctions = detect_conjunctions(
        planet_positions
    )

    # =========================
    # YOGAS
    # =========================

    yogas = detect_yogas(
        planet_positions
    )

    return {
        "report": report,
        "conjunctions": conjunctions,
        "yogas": yogas
    }
