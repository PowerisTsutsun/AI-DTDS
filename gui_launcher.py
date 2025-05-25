import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import ctypes

# Request admin permissions on Windows
def request_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

# Start real-time detector
def start_detector():
    global detector_process
    if detector_process and detector_process.poll() is None:
        messagebox.showinfo("Info", "Detector already running!")
        return
    detector_process = subprocess.Popen(["python", "src/real_time_detector.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    messagebox.showinfo("Info", "Detector started.")


# Start Streamlit dashboard
def start_dashboard():
    global dashboard_process
    if dashboard_process and dashboard_process.poll() is None:
        messagebox.showinfo("Info", "Dashboard already running!")
        return
    dashboard_process = subprocess.Popen(["streamlit", "run", "dashboard.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    messagebox.showinfo("Info", "Dashboard started at http://localhost:8501")


# Stop both processes
def stop_all():
    if detector_process and detector_process.poll() is None:
        detector_process.terminate()
    if dashboard_process and dashboard_process.poll() is None:
        dashboard_process.terminate()
    messagebox.showinfo("Info", "Stopped detector and dashboard.")

# Main GUI
if __name__ == '__main__':
    detector_process = None
    dashboard_process = None

    if not request_admin():
        sys.exit()

    root = tk.Tk()
    root.title("Threat Detection Control Panel")
    root.geometry("400x250")

    tk.Label(root, text="Threat Detection System", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Start Real-Time Detector", width=30, command=start_detector).pack(pady=5)
    tk.Button(root, text="Start Streamlit Dashboard", width=30, command=start_dashboard).pack(pady=5)
    tk.Button(root, text="Stop All", width=30, command=stop_all).pack(pady=5)
    tk.Button(root, text="Exit", width=30, command=root.destroy).pack(pady=5)

    root.mainloop()
