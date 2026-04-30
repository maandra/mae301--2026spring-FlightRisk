FlightRisk
FlightRisk is a Streamlit app that ranks flight options by disruption risk and adds a budget aware comparison layer.

What is Included:
  1. app.py: Streamlit app entry point
  2. src/flightrisk/: model loading, feature engineering, and prediction code
  3. artifacts/flight_risk_bundle.joblib: trained model bundle used by the app
  4. artifacts/metrics.json: model metrics from training
  5. flight_dataset.csv: fare prediction reference data used by the budget layer
  6. requirements.txt: Python dependencies for Streamlit Cloud
  7. .streamlit/config.toml: basic Streamlit display settings

Running The Program:
Option 1: In order to simply access the app, a link to the FlightRisk App is included here:
[https://flightriskfinal-mae301.streamlit.app/](https://flightriskfinal-mae301.streamlit.app/)
This is the simplest and recommended method. If the Streamlit App appears to be asleep, simply use the option to wake it.

Option 2: If you wish to set up the app for local use by using the provided code, follow these instructions:
→ Environmental Setup and Information
   - Use Python 3.11 or newer
→ Clone From GitHub and Run Locally
   - Install Dependencies: powershell python -m pip install -r requirements.txt
   - Run the Steamlit app: powershell python -m streamlit run app.py
   - Then Open: http://localhost:8501
