# alerts.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# ⚙️ YOUR SETTINGS — fill these in!
EMAIL_SENDER   = "puligadeviprasad@gmail.com"
EMAIL_PASSWORD = "xsmabdzhmdyjhoml"
EMAIL_RECEIVER = "puligadeviprasad@gmail.com"
SMTP_SERVER    = "smtp.gmail.com"
SMTP_PORT      = 587

def send_alert(subject, message):
    try:
        msg = MIMEMultipart()
        msg["From"]    = EMAIL_SENDER
        msg["To"]      = EMAIL_RECEIVER
        msg["Subject"] = subject

        body = f"""
Linux Monitor Alert
-------------------
Time    : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Server  : linux-monitor-server

{message}

-------------------
Sent by Linux Monitor
        """
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        print(f"[EMAIL SENT] {subject}")
        return True

    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return False

def check_and_alert(metrics):
    THRESHOLDS = {
        "cpu":    80,
        "memory": 75,
        "disk":   85,
    }
    for key, limit in THRESHOLDS.items():
        if metrics.get(key, 0) > limit:
            subject = f"[ALERT] {key.upper()} usage critical on linux-monitor-server"
            message = f"{key.upper()} is at {metrics[key]:.1f}% — threshold is {limit}%"
            send_alert(subject, message)

if __name__ == "__main__":
    # Test email
    send_alert(
        subject="[TEST] Linux Monitor is working!",
        message="This is a test email from your Linux monitoring project."
    )
