import os, joblib
import streamlit as st
import pandas as pd, joblib, json
from pathlib import Path

st.set_page_config(page_title="VO₂ Max & Training Readiness", page_icon="🏃", layout="centered")
st.title("🏃 VO₂ Max & Training Readiness (Synthetic, Demo)")
st.caption("CPU-only • Synthetic data • Not medical advice.")

DATA_PATH = "assets/vo2_real_augmented.csv"

#MODEL_PATH = "model/vo2_predictor.joblib"
#MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "vo2_predictor.joblib")

HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "model" / "vo2_predictor.joblib"   # src/model/...
# If your model is at repo_root/model, use: HERE.parent / "model" / "vo2_predictor.joblib"

print("CWD:", os.getcwd())
print("Script dir:", HERE)
print("Listing script dir:", list(HERE.iterdir()))
print("Listing model dir:", list((HERE / "model").glob("*")))

assert MODEL_PATH.exists(), f"Model not found at: {MODEL_PATH}"

pipe = joblib.load(MODEL_PATH)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_sample():
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception:
        return pd.DataFrame()

pipe = load_model()
df = load_sample()

with st.expander("Sample data (first 50 rows)"):
    if not df.empty:
        st.dataframe(df.head(50), use_container_width=True)
    else:
        st.info("Sample CSV not found.")

st.subheader("Enter runner metrics")
cols = st.columns(2)

sex = cols[0].selectbox("Sex (0=female, 1=male)", [0,1], index=1)
age = cols[1].slider("Age", 18, 70, 35)
height_cm = cols[0].slider("Height (cm)", 150, 200, 172)
weight_kg = cols[1].slider("Weight (kg)", 45, 120, 74)

total_lean_mass = cols[0].slider("Total Lean Mass", 30, 90, 55)
wbtpf = cols[1].slider("Whole Body Tissue Percent Fat", 12, 49, 28)

resting_hr = cols[0].slider("Resting HR (bpm)", 40, 100, 60)
max_hr = cols[1].slider("Max HR (bpm)", 150, 205, 185)
avg_hr_during_run = cols[0].slider("Avg HR During Run (bpm)", 95, 190, 150)
hr_recovery_1min = cols[1].slider("HR Recovery 1 min (bpm drop)", 10, 55, 30)

distance_km = cols[0].slider("Distance of last run (km)", 1, 30, 5)
duration_min = cols[1].slider("Duration of last run (min)", 10, 180, 30)
pace_min_per_km = max(3.5, min(12.0, duration_min / max(distance_km, 0.5)))
avg_speed_kmh = 60.0 / pace_min_per_km
elevation_gain_m = cols[0].slider("Elevation Gain (m)", 0, 600, 50)

training_hours_week = cols[1].slider("Training Hours / Week", 0, 12, 4)
avg_intensity = cols[0].slider("Avg Intensity (1–10)", 1, 10, 6)
rest_days = cols[1].slider("Rest Days (last 7d)", 0, 4, 1)

sleep_hours_last_night = cols[0].slider("Sleep Hours Last Night", 3, 10, 7)
avg_sleep_hours_week = cols[1].slider("Avg Sleep Hours / Week", 4, 9, 7)
sleep_quality_score = cols[0].slider("Sleep Quality (0–100)", 25, 95, 72)
resting_hr_delta = resting_hr - 60

temperature_C = cols[1].slider("Temperature (°C)", 0, 35, 18)
humidity_pct = cols[0].slider("Humidity (%)", 15, 95, 55)
altitude_m = cols[1].slider("Altitude (m)", 0, 2200, 200)

hr_ratio = avg_hr_during_run / max_hr if max_hr>0 else 0
training_load_index = distance_km * (avg_hr_during_run/100.0) / (duration_min/60.0 + 0.1)
speed_per_kg = avg_speed_kmh / (weight_kg/70.0)

features = {
 "sex":sex,"age":age,"height_cm":height_cm,"weight_kg":weight_kg,
 "bmi": weight_kg/((height_cm/100.0)**2),
 "resting_hr":resting_hr,"max_hr":max_hr,"avg_hr_during_run":avg_hr_during_run,
 "hr_recovery_1min":hr_recovery_1min,
 "distance_km":distance_km,"duration_min":duration_min,
 "pace_min_per_km":pace_min_per_km,"avg_speed_kmh":avg_speed_kmh,
 "elevation_gain_m":elevation_gain_m,
 "training_hours_week":training_hours_week,"avg_intensity":avg_intensity,"rest_days":rest_days,
 "sleep_hours_last_night":sleep_hours_last_night,"avg_sleep_hours_week":avg_sleep_hours_week,
 "sleep_quality_score":sleep_quality_score,"resting_hr_delta":resting_hr_delta,
 "temperature_C":temperature_C,"humidity_pct":humidity_pct,"altitude_m":altitude_m,
 "hr_ratio":hr_ratio,"training_load_index":training_load_index,"speed_per_kg":speed_per_kg
}

def coaching_tip(vo2, sleep_quality, training_hours, hrr):
    tips = []
    if vo2 < 38: tips.append("Prioritize easy aerobic runs (Zone 2) 3–4x/week.")
    elif vo2 < 48: tips.append("Add 1 weekly interval (e.g., 4×4min hard, full recovery).")
    else: tips.append("Maintain with polarized training; 80% easy, 20% hard.")

    if sleep_quality < 60: tips.append("Boost sleep hygiene to 7–8h; reduce late caffeine/screens.")
    if training_hours > 8: tips.append("High load detected — deload 10–20% this week.")
    if hrr < 20: tips.append("Low HRR — keep intensities sub-threshold for 2–3 days.")
    return " ".join(tips) or "Keep up the good work!"

if st.button("Predict VO₂ max"):
    x = pd.DataFrame([features])
    pipe = load_model()
    vo2 = float(pipe.predict(x)[0])
    tip = coaching_tip(vo2, sleep_quality_score, training_hours_week, hr_recovery_1min)

    st.metric("Estimated VO₂ max (ml/kg/min)", f"{vo2:.1f}")
    st.success(tip)

st.divider()
st.caption("Limitations: Synthetic data; not a medical device; demo use only.")
