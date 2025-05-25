import time
import win32evtlog

def listen_logs(log_file_path='data/raw/syslog_example.log'):
    # Try utf-8-sig first; fallback to latin-1 if necessary
    try:
        file = open(log_file_path, 'r', encoding='utf-8-sig')
    except UnicodeDecodeError:
        file = open(log_file_path, 'r', encoding='latin-1')

    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


def listen_windows_logs(server='localhost', log_type='Security'):
    print(f"Listening to Windows Event Logs: {log_type}")
    hand = win32evtlog.OpenEventLog(server, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if events:
            for ev_obj in events:
                yield str(ev_obj.StringInserts)
        else:
            time.sleep(1)
