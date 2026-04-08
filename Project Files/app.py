from __future__ import annotations

from datetime import date
from pathlib import Path
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from flightrisk.predictor import FlightRiskPredictor


st.set_page_config(page_title="Flight Risk", layout="wide")

BUNDLE_PATH = PROJECT_ROOT / "artifacts" / "flight_risk_bundle.joblib"

st.title("Flight Risk")
st.caption("Prototype flight disruption ranking tool built from historical flight and weather data.")

if not BUNDLE_PATH.exists():
    st.error(
        "No trained model bundle was found. Train the model first with "
        "`python train_model.py --data-path flights_with_weather.parquet --output-dir artifacts`."
    )
    st.stop()

predictor = FlightRiskPredictor.load(BUNDLE_PATH)

col1, col2, col3 = st.columns(3)
with col1:
    origin = st.text_input("Origin airport", value="LAX").strip().upper()
with col2:
    destination = st.text_input("Destination airport", value="SLC").strip().upper()
with col3:
    travel_date = st.date_input("Travel date", value=date.today())

airlines = predictor.available_airlines_for_route(origin, destination)
selected_airline = st.selectbox("Airline filter", options=["Any"] + airlines, index=0)
top_n = st.slider("How many options to show", min_value=3, max_value=15, value=8)

if st.button("Rank Flight Options", type="primary"):
    airline_filter = None if selected_airline == "Any" else selected_airline
    results = predictor.rank_route_options(
        origin=origin,
        destination=destination,
        flight_date=pd.Timestamp(travel_date),
        airline_code=airline_filter,
        top_n=top_n,
    )

    if results.empty:
        st.warning("No historical route options were found for that route and airline selection.")
    else:
        display_cols = [
            "flight_code",
            "airline_code",
            "departure_time",
            "distance",
            "scheduled_elapsed_time",
            "risk_score",
            "on_time",
            "short_delay",
            "long_delay",
            "cancelled",
            "historical_support",
            "explanation",
        ]
        formatted = results[display_cols].copy()
        probability_cols = ["risk_score", "on_time", "short_delay", "long_delay", "cancelled"]
        for col in probability_cols:
            formatted[col] = formatted[col].map(lambda value: f"{value:.1%}")
        st.dataframe(formatted, use_container_width=True, hide_index=True)

        best = results.iloc[0]
        st.success(
            f"Lowest-risk option: {best['airline_code']} at {best['scheduled_departure']} "
            f"with risk score {best['risk_score']:.1%}."
        )
