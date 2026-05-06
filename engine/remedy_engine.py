import pandas as pd

remedies_df = pd.read_csv(
    "data/remedies.csv"
)

# =========================
# STATES THAT NEED REMEDY
# =========================

NEGATIVE_STATES = [
    "weak",
    "combust",
    "debilitated",
    "afflicted"
]

def get_remedies(
    planet,
    state=None
):

    # =========================
    # GOOD PLANETS
    # =========================

    if state not in NEGATIVE_STATES:

        return [
            "No major remedy required."
        ]

    # =========================
    # FILTER REMEDIES
    # =========================

    result = remedies_df[
        (remedies_df["planet"] == planet)
        &
        (remedies_df["state"] == state)
    ]

    remedies = []

    for _, row in result.iterrows():

        remedies.append(
            row["remedy"]
        )

    # =========================
    # DEFAULT
    # =========================

    if len(remedies) == 0:

        remedies.append(
            "Maintain positive discipline and spirituality."
        )

    return remedies
