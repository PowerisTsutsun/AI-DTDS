# 🚨 AI-Driven Threat Detection System  

An **automated real-time threat detection system** powered by an Isolation Forest model and enhanced with a **GUI launcher** and **Streamlit dashboard** for monitoring.  

## 🔥 Features
- ✅ Real-time log ingestion from **Windows Event Logs** or file-based logs.  
- ✅ AI-driven anomaly detection using **Isolation Forest**.  
- ✅ **GUI launcher** (`gui_launcher.py`) with admin permission handling.  
- ✅ **Command-line launcher** (`run.py`) for full system startup.  
- ✅ **Streamlit dashboard** for real-time monitoring of suspicious logs.  
- ✅ Modular and extensible for future improvements.

## 📂 Project Structure

```
AI-Driven Threat Detection System/
├── data/
│ ├── raw/
│ └── processed/
├── model/
│ └── train_model.py
├── src/
│ ├── feature_extraction.py
│ ├── log_listener.py
│ ├── windows_log_listener.py
│ └── real_time_detector.py
├── dashboard.py
├── append_logs.py
├── gui_launcher.py
├── run.py
└── README.md

```



## 🚀 Quick Start

### 🔸 Option 1: GUI Launcher
1️⃣ Run:

 - python gui_launcher.py

2️⃣ Approve the admin permission prompt.  
3️⃣ Use the GUI to:
- Start real-time detector (Windows Event Logs or file logs).
- Start the Streamlit dashboard at `http://localhost:8501`.
- Stop the system.

### 🔸 Option 2: Command-Line Launcher
1️⃣ Run:

 - python run.py

 2️⃣ This will:
- Train the model if missing.
- Start real-time detector.
- Launch the Streamlit dashboard.

## ⚙️ Dependencies
- Python 3.11+  
- Required packages:

```pip install streamlit pandas scikit-learn pywin32```


## 📈 Dashboard
- Accessible at `http://localhost:8501`.
- Displays **real-time suspicious logs** detected by the system.
- Auto-refreshes every 5 seconds with dynamic countdown.

## 🔒 Admin Permissions
- Required for **Windows Event Log access**.
- The **GUI launcher requests permissions automatically**.

## 💡 Future Improvements
- Enhanced feature extraction and supervised model training.
- Switchable log source selection in GUI.
- Professional-grade GUI (PyQt/Kivy).
- Deployment as a standalone EXE (PyInstaller).

## 🏆 Contributors
- PowerisTsutsun 