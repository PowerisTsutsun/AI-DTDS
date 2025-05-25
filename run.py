import subprocess
import os
import threading
import time
import sys

def train_model_if_needed():
    model_path = 'model/isolation_forest.pkl'
    if not os.path.exists(model_path):
        print("🔨 Model not found. Training model...")
        subprocess.run([sys.executable, 'model/train_model.py'])
    else:
        print("✅ Model already exists. Skipping training.")

def start_real_time_detector():
    print("🚨 Starting real-time detection...")
    subprocess.run([sys.executable, 'src/real_time_detector.py'])

def start_dashboard():
    print("📊 Launching Streamlit dashboard...")
    subprocess.run(['streamlit', 'run', 'dashboard.py'])

if __name__ == '__main__':
    train_model_if_needed()

    # Run real-time detector in a separate thread
    detector_thread = threading.Thread(target=start_real_time_detector)
    detector_thread.start()

    # Delay to ensure detector starts first
    time.sleep(2)

    # Start Streamlit dashboard in main thread
    start_dashboard()
