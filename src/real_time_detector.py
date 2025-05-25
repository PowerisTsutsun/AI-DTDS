import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from src.log_listener import listen_logs
from src.windows_log_listener import listen_windows_logs
import joblib
import pandas as pd
import threading
from src.feature_extraction import extract_features

# Import both log listeners
from src.log_listener import listen_logs
from src.windows_log_listener import listen_windows_logs

def load_model(model_path='model/isolation_forest.pkl'):
    return joblib.load(model_path)

def main():
    model = load_model()
    print("✅ Model loaded. Starting real-time detection...")

    suspicious_logs = []

    # Choose log source
    use_windows_logs = True  # Set to False if you want to use file logs

    if use_windows_logs:
        log_source = listen_windows_logs()
    else:
        log_source = listen_logs()

    for log_line in log_source:
        features = extract_features(log_line)
        if features is not None:
            X = pd.DataFrame([features])
            prediction = model.predict(X)[0]
            if prediction == -1:
                print(f"⚠️ Threat detected: {log_line.strip()}")
                suspicious_logs.append(log_line.strip())

                pd.DataFrame(suspicious_logs, columns=['log']).to_csv('data/processed/suspicious_logs.csv', index=False)

                # Trigger scan
                trigger_scan(log_line)

def trigger_scan(log_line):
    print(f"🔍 Triggering vulnerability scan for log: {log_line.strip()}")

if __name__ == "__main__":
    main()
