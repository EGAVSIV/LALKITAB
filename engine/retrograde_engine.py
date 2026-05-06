import swisseph as swe

def is_retrograde(jd, planet_id):

    data = swe.calc_ut(jd, planet_id)

    speed = data[0][3]

    return speed < 0
