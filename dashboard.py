import streamlit as st
import pandas as pd
import os
import time

LOG_FILE = 'data/processed/suspicious_logs.csv'

st.title("🚨 Threat Detection Dashboard")

refresh_rate = 5  # seconds

def load_logs():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    else:
        return pd.DataFrame(columns=['log'])

st.subheader("Flagged Suspicious Logs")
logs = load_logs()

if not logs.empty:
    st.table(logs)
else:
    st.info("No suspicious logs detected yet.")

# Dynamic timer display
timer_placeholder = st.empty()

for remaining in range(refresh_rate, 0, -1):
    timer_placeholder.text(f"Auto-refreshing in {remaining} seconds...")
    time.sleep(1)

st.rerun()
