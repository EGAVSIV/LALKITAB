import swisseph as swe

def calculate_houses(jd, lat, lon):

    houses, ascmc = swe.houses(jd, lat, lon, b'P')

    ascendant = ascmc[0]

    return houses, ascendant

def get_house(planet_degree, ascendant):

    diff = (planet_degree - ascendant) % 360

    house = int(diff / 30) + 1

    return house
