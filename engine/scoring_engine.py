def calculate_strength(state):

    score_map = {
        "strong": 90,
        "weak": 40,
        "afflicted": 30,
        "combust": 25
    }

    return score_map.get(state, 50)
