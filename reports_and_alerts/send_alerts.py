import pandas as pd
import smtplib
from email.message import EmailMessage

THREAT_DATA_PATH = 'detected_threats.csv'
ALERT_EMAIL = 'admin@example.com'
ALERT_THRESHOLD = 5  

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_SENDER = 'sarkar@gmail.com'
EMAIL_PASSWORD = 'debroop123'  

def send_email_alert(subject, content):
    msg = EmailMessage()
    msg['From'] = EMAIL_SENDER
    msg['To'] = ALERT_EMAIL
    msg['Subject'] = subject
    msg.set_content(content)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

def check_and_alert():
    try:
        df = pd.read_csv(THREAT_DATA_PATH)

        threat_counts = df['threat_type'].value_counts()

        if 'Failed password' in threat_counts and threat_counts['Failed password'] > ALERT_THRESHOLD:
            alert_msg = f"High number of failed password attempts detected: {threat_counts['Failed password']}"
            print(alert_msg)

            send_email_alert(" Security Alert: Failed Logins", alert_msg)

        else:
            print("No critical alerts detected.")

    except Exception as e:
        print(f"Error during alert check: {e}")

if __name__ == '__main__':
    check_and_alert()
