# log_parser.py
import re, datetime

LOG_FILE = "/var/log/syslog"

PATTERNS = {
    "auth_fail":  r"authentication failure|Failed password",
    "oom":        r"Out of memory|oom-kill",
    "disk_error": r"I/O error|disk error",
    "crash":      r"segfault|kernel panic",
}

def parse_logs():
    found = []
    try:
        with open(LOG_FILE, "r", errors="ignore") as f:
            for line in f:
                for name, pattern in PATTERNS.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        found.append((name, line.strip()))
    except PermissionError:
        print("Need sudo to read syslog. Run:  sudo python3 log_parser.py")
        return []
    return found

def report():
    results = parse_logs()
    if not results:
        print("No anomalies found — system logs are clean!")
        return
    print(f"\n=== Log Anomaly Report — {datetime.date.today()} ===")
    by_type = {}
    for name, line in results:
        by_type.setdefault(name, []).append(line)
    for name, lines in by_type.items():
        print(f"\n[{name.upper()}] — {len(lines)} occurrences")
        for l in lines[-3:]:
            print(f"  {l[:100]}")

if __name__ == "__main__":
    report()
