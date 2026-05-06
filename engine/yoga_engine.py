def detect_yogas(planets):

    yogas = []

    if abs(planets["Moon"] - planets["Jupiter"]) <= 10:

        yogas.append("Gaj Kesari Yoga")

    if abs(planets["Sun"] - planets["Mercury"]) <= 10:

        yogas.append("Budh Aditya Yoga")

    if abs(planets["Moon"] - planets["Mars"]) <= 10:

        yogas.append("Chandra Mangal Yoga")

    return yogas
