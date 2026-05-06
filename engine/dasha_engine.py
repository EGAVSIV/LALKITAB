def get_current_dasha(moon_degree):

    nakshatra = int(moon_degree / (360 / 27))

    dasha_sequence = [
        "Ketu",
        "Venus",
        "Sun",
        "Moon",
        "Mars",
        "Rahu",
        "Jupiter",
        "Saturn",
        "Mercury"
    ]

    return dasha_sequence[nakshatra % 9]
