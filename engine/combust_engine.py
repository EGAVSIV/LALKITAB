COMBUST_LIMITS = {
    "Mars": 17,
    "Mercury": 14,
    "Jupiter": 11,
    "Venus": 10,
    "Saturn": 15
}

def check_combust(planet, planet_degree, sun_degree):

    if planet not in COMBUST_LIMITS:
        return False

    diff = abs(planet_degree - sun_degree)

    if diff > 180:
        diff = 360 - diff

    return diff <= COMBUST_LIMITS[planet]
