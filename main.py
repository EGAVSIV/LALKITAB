import streamlit as st

from engine.astrology_engine import analyze_chart
from engine.location_engine import get_location_data

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Lal Kitab AI",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🔮 Lal Kitab AI Astrology Software")

st.markdown("---")

# =========================
# SIDEBAR INPUTS
# =========================

st.sidebar.header("Birth Details")

dob = st.sidebar.text_input(
    "DOB (YYYY-MM-DD)",
    "1983-06-02"
)

tob = st.sidebar.text_input(
    "Time (HH:MM)",
    "22:15"
)

place = st.sidebar.text_input(
    "Birth Place",
    "Bharatpur Rajasthan India"
)

# =========================
# ANALYZE BUTTON
# =========================

if st.sidebar.button("Generate Kundali"):

    try:

        # =========================
        # LOCATION
        # =========================

        location_data = get_location_data(
            place
        )

        lat = location_data["latitude"]

        lon = location_data["longitude"]

        timezone = location_data["timezone"]

        # =========================
        # ANALYZE
        # =========================

        result = analyze_chart(
            dob,
            tob,
            lat,
            lon,
            timezone
        )

        report = result["report"]

        conjunctions = result["conjunctions"]

        yogas = result["yogas"]

        # =========================
        # LOCATION INFO
        # =========================

        st.subheader("📍 Location Details")

        st.write(f"Place: {place}")

        st.write(f"Latitude: {lat}")

        st.write(f"Longitude: {lon}")

        st.write(f"Timezone: {timezone}")

        st.markdown("---")

        # =========================
        # PLANET REPORT
        # =========================

        st.subheader("🪐 Planet Analysis")

        for item in report:

            with st.expander(
                f"{item['planet']} | House {item['house']} | {item['state']}"
            ):

                st.write(
                    f"Degree: {item['degree']}"
                )

                st.write(
                    f"State: {item['state']}"
                )

                if item["manglik"]:

                    st.error(
                        "Manglik Dosha Detected"
                    )

                # =========================
                # PREDICTIONS
                # =========================

                st.markdown("### Predictions")

                for p in item["predictions"]:

                    st.write(f"✅ {p}")

                # =========================
                # REMEDIES
                # =========================

                st.markdown("### Remedies")

                for r in item["remedies"]:

                    if r == "No major remedy required.":

                        st.success(r)

                    else:

                        st.warning(r)

        st.markdown("---")

        # =========================
        # CONJUNCTIONS
        # =========================

        st.subheader("☄️ Conjunctions")

        if conjunctions:

            for c in conjunctions:

                st.write(f"🔹 {c}")

        else:

            st.write(
                "No major conjunctions found."
            )

        st.markdown("---")

        # =========================
        # YOGAS
        # =========================

        st.subheader("✨ Yogas")

        if yogas:

            for y in yogas:

                st.write(f"🌟 {y}")

        else:

            st.write(
                "No major yogas detected."
            )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )
