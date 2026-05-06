import pandas as pd

rules_df = pd.read_csv(
    "data/planet_rules.csv"
)

def get_prediction(
    planet,
    house,
    state
):

    predictions = []

    # =========================
    # EXACT MATCH
    # =========================

    exact = rules_df[
        (rules_df["planet"] == planet)
        &
        (rules_df["house"] == house)
        &
        (rules_df["state"] == state)
    ]

    # =========================
    # IF EXACT FOUND
    # =========================

    if not exact.empty:

        for _, row in exact.iterrows():

            predictions.append(
                row["prediction"]
            )

    # =========================
    # FALLBACK MATCH
    # =========================

    else:

        fallback = rules_df[
            (rules_df["planet"] == planet)
            &
            (rules_df["house"] == house)
        ]

        for _, row in fallback.iterrows():

            predictions.append(
                row["prediction"]
            )

    # =========================
    # DEFAULT MESSAGE
    # =========================

    if len(predictions) == 0:

        predictions.append(
            "General planetary influence active."
        )

    return predictions
