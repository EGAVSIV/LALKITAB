def detect_conjunctions(planets):

    conjunctions = []

    names = list(planets.keys())

    for i in range(len(names)):

        for j in range(i + 1, len(names)):

            p1 = names[i]
            p2 = names[j]

            d1 = planets[p1]
            d2 = planets[p2]

            diff = abs(d1 - d2)

            if diff > 180:
                diff = 360 - diff

            if diff <= 8:

                conjunctions.append(
                    f"{p1} conjunct {p2}"
                )

    return conjunctions
