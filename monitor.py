# monitor.py
import psutil, time, datetime
from alerts import send_alert
from database import create_table, save_metrics

THRESHOLDS = {
    "cpu":    80,
    "memory": 75,
    "disk":   85,
}

def get_metrics():
    return {
        "cpu":    psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk":   psutil.disk_usage("/").percent,
        "net_in": psutil.net_io_counters().bytes_recv,
        "net_out":psutil.net_io_counters().bytes_sent,
    }

def check_alerts(metrics):
    for key, limit in THRESHOLDS.items():
        value = metrics.get(key, 0)
        if value > limit:
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[ALERT {ts}] {key.upper()} at {value:.1f}% — threshold {limit}%")
            subject = f"[ALERT] {key.upper()} is high on your server!"
            message = f"{key.upper()} is at {value:.1f}% — threshold is {limit}%"
            send_alert(subject, message)

def run():
    create_table()
    print("Monitoring started. Press Ctrl+C to stop.\n")
    while True:
        m = get_metrics()
        print(f"CPU: {m['cpu']:.1f}%  MEM: {m['memory']:.1f}%  DISK: {m['disk']:.1f}%")
        check_alerts(m)
        save_metrics(m)
        time.sleep(5)

if __name__ == "__main__":
    run()
