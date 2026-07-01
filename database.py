# database.py
import sqlite3
import datetime

DB_FILE = "metrics.db"

def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu       REAL,
            memory    REAL,
            disk      REAL,
            net_in    INTEGER,
            net_out   INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_metrics(metrics):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO metrics (timestamp, cpu, memory, disk, net_in, net_out)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        metrics["cpu"],
        metrics["memory"],
        metrics["disk"],
        metrics["net_in"],
        metrics["net_out"]
    ))
    conn.commit()
    conn.close()
    print(f"[DB SAVED] Metrics saved to database")

def show_history():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM metrics ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    print("\n=== Last 10 Metric Readings ===")
    print(f"{'ID':<5} {'Timestamp':<22} {'CPU':<8} {'Memory':<8} {'Disk':<8}")
    print("-" * 55)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<22} {row[2]:<8.1f} {row[3]:<8.1f} {row[4]:<8.1f}")

if __name__ == "__main__":
    create_table()
    print("Database created successfully!")
    show_history()
