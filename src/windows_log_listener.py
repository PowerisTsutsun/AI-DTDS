import time
import win32evtlog

def listen_windows_logs(server='localhost', log_type='Security'):
    print(f"🔍 Listening to Windows Event Logs: {log_type}")
    hand = win32evtlog.OpenEventLog(server, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if events:
            for ev_obj in events:
                yield str(ev_obj.StringInserts)
        else:
            time.sleep(1)
