import time
import random

log_file = 'data/raw/syslog_example.log'
new_lines = [
    "Jan 10 12:30:00 myhost sshd[12345]: Failed password for user hacker from 192.168.1.50 port 22 ssh2",
    "Jan 10 12:31:00 myhost sshd[12345]: Accepted password for user alice from 192.168.1.11 port 22 ssh2",
    "Jan 10 12:32:00 myhost sshd[12345]: Failed password for user admin from 192.168.1.12 port 22 ssh2",
    "Jan 10 12:33:00 myhost sshd[12345]: Failed password for user bob from 192.168.1.14 port 22 ssh2",
    "Jan 10 12:34:00 myhost sshd[12345]: Accepted password for user charlie from 192.168.1.15 port 22 ssh2",
    "Jan 10 12:35:00 myhost sshd[12345]: Failed password for user root from 192.168.1.16 port 22 ssh2"
]

print("📢 Random log appender is running...")

with open(log_file, 'a', encoding='utf-8') as f:
    for _ in range(10):  # Append 10 random entries
        line = random.choice(new_lines)
        f.write(line + '\n')
        print(f"Added: {line}")
        time.sleep(random.uniform(1, 3))  # Random delay between 1 and 3 seconds

print("✅ Finished appending logs.")
