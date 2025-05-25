import re

def extract_features(log_line):
    """
    Extract features from a raw log line.
    Example assumes syslog-like format.
    """
    # Example: Jan 10 12:00:00 hostname process[pid]: message
    match = re.match(r'(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+(\S+):\s+(.*)', log_line)
    if match:
        timestamp, host, process, message = match.groups()
        features = {
            'packet_size': len(message),
            'access_frequency': 1,  # Placeholder
            'failed_logins': 1 if 'failed' in message.lower() else 0,
            'ip_entropy': 1.5  # Placeholder, can enhance later
        }
        return features
    return None
