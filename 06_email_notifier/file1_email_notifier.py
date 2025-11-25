# Email Notifier - file1

import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
password = "your_password"
receiver = input("Enter receiver email: ")

msg = MIMEText("This is an automated notification!")
msg["Subject"] = "Notification"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Email sent!")
