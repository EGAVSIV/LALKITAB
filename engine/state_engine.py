from engine.combust_engine import check_combust
from engine.exaltation_engine import EXALTED
from engine.exaltation_engine import DEBILITATED

# Zodiac Signs
SIGNS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
]

def get_sign(degree):

    sign_index = int(degree / 30)

    return SIGNS[sign_index]

def determine_planet_state(
    planet,
    degree,
    sun_degree
):

    sign = get_sign(degree)

    # =========================
    # COMBUST CHECK
    # =========================

    if check_combust(
        planet,
        degree,
        sun_degree
    ):

        return "combust"

    # =========================
    # EXALTED CHECK
    # =========================

    if planet in EXALTED:

        if sign == EXALTED[planet]:

            return "exalted"

    # =========================
    # DEBILITATED CHECK
    # =========================

    if planet in DEBILITATED:

        if sign == DEBILITATED[planet]:

            return "debilitated"

    # =========================
    # SIMPLE WEAK/STRONG LOGIC
    # =========================

    if sign in [
        "Aries",
        "Leo",
        "Sagittarius"
    ]:

        return "strong"

    if sign in [
        "Cancer",
        "Scorpio",
        "Pisces"
    ]:

        return "weak"

    return "normal"
