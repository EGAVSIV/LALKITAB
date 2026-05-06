import swisseph as swe

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE
}

def get_planet_positions(jd):

    positions = {}

    for name, planet in PLANETS.items():

        degree = swe.calc_ut(jd, planet)[0][0]

        positions[name] = round(degree, 2)

    return positions
